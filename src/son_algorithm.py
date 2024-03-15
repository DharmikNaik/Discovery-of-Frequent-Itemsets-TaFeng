from pyspark import RDD
import src.apriori as apriori
from math import floor
from operator import add
from src.transformations import parseDfBasketsToList
import time


def generateLocalFrequentItemsets(partition, supportThreshold: int, countBaskets: int, basketsInDfRow: bool):
    if basketsInDfRow:
        partition = parseDfBasketsToList(partition)
    countPartitionBaskets = len(partition)
    scaledDownSupport = floor(countPartitionBaskets / countBaskets * supportThreshold)
    return apriori.getFrequentItemsets(partition, scaledDownSupport)

def emitItemsetsCount(record, itemsets):
    basketItems = set(record.BASKET)
    return [(itemset, 1) for itemset in itemsets if itemset.is_subset_of(basketItems)]


def getFrequentItemsets(rddBaskets: RDD, supportThreshold: int, basketsInDfRow: bool = True):
    startTime = time.time()
    countBaskets = rddBaskets.count()
    candidateFrequentItemsets = rddBaskets.mapPartitions(lambda partition: generateLocalFrequentItemsets(partition, supportThreshold, countBaskets, basketsInDfRow))\
        .distinct()\
        .collect()

    frequentItemsets = rddBaskets.flatMap(lambda record: emitItemsetsCount(record, candidateFrequentItemsets))\
        .reduceByKey(add)\
        .filter(lambda itemsetFrequencyPair: itemsetFrequencyPair[1] >= supportThreshold)\
        .map(lambda itemsetFrequencyPair: itemsetFrequencyPair[0])\
        .collect()
    endTime = time.time()
    print(endTime - startTime)
    return frequentItemsets

