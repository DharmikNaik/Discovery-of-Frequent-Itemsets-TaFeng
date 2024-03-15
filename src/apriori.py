from itertools import combinations
from src.utils import flattenList
from collections import defaultdict
from src.itemset import Itemset


def generateSingletonItemsets(baskets):
    itemCounts = defaultdict(lambda: 0)
    for basket in baskets:
        for item in basket:
            itemset = Itemset([item])
            itemCounts[itemset] += 1
    return itemCounts



def generateCandidateItemsets(baskets: list, itemsetSize: int, frequentItemsets: list):
    if itemsetSize == 1:
        return generateSingletonItemsets(baskets)
    else:
        uniqueItemsFromFrequentItemsets = {item for itemset in frequentItemsets for item in itemset.items}
        candidateItemsets = defaultdict(lambda: 0)
        for basket in baskets:
            basketItems = set(basket)
            filteredItems = basketItems.intersection(uniqueItemsFromFrequentItemsets)
            for itemCombination in combinations(filteredItems, itemsetSize):
                itemset = Itemset(itemCombination)
                candidateItemsets[itemset] += 1
        return candidateItemsets

def getItemsetsFrequency(itemsets, baskets):
    itemsetFrequency = defaultdict(lambda: 0)
    for basket in baskets:
        basketItems = set(tuple(basket))
        for itemset in itemsets:
            if itemset.is_subset_of(basketItems):
                itemsetFrequency[itemset] += 1
    return itemsetFrequency

def pruneInfrequentItemsets(candidateItemsets, support):
    frequentItemsets = [itemset for itemset, freq in candidateItemsets.items() if freq >= support]
    return frequentItemsets

def getFrequentItemsets(baskets: list, support: int):
    itemsetSize: int = 1
    frequentItemsets: list[list[Itemset]] = list()
    while True:
        if itemsetSize == 1:
            candidateItemsets = generateCandidateItemsets(baskets, itemsetSize, None)
        else:
            candidateItemsets = generateCandidateItemsets(baskets, itemsetSize, frequentItemsets[-1])
        if(not candidateItemsets):
            break
        trueFrequentItemsets = pruneInfrequentItemsets(candidateItemsets, support)
        if not trueFrequentItemsets:
            break
        frequentItemsets.append(trueFrequentItemsets)
        itemsetSize += 1
    return flattenList(frequentItemsets)
