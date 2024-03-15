from src.config_parser import config
from pyspark.sql import SparkSession
from src.data_loader import loadData
from src.out import outputData
from src.son_algorithm import getFrequentItemsets
import time

def setupSpark() -> SparkSession:
    spark = SparkSession.builder \
        .appName("MarketBasketAnalysis") \
        .getOrCreate()
    return spark

# def setupLogging(sparkContext: SparkContext):
#     sparkContext.setLogLevel('INFO')

def main():
    sparkSession = setupSpark()
    # setupLogging(sparkContext)
    rddBaskets = loadData(config, sparkSession)
    frequentItemsets = getFrequentItemsets(rddBaskets, int(config['apriori_params']['suppport_threshold']))
    outputData(frequentItemsets, config)
    sparkSession.stop()


if __name__ == '__main__':
    main()