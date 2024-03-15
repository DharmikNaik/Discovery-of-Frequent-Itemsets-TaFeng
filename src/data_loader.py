from configparser import ConfigParser
from src.schemas import rawDataSchema
from pyspark.sql import SparkSession, DataFrame
from src.transformations import preprocessData, generateBaskets
from src.constants import PROJECT_ROOT
import os
from src.out import writeBaskets


def loadData(config: ConfigParser, sparkSession: SparkSession) -> DataFrame:
    inputFilePath = os.path.join(PROJECT_ROOT, config['file_paths']['input_path'])
    dfRawData = sparkSession.read.csv(inputFilePath, header=True, schema=rawDataSchema, quote='"')
    dfPreprocessed = preprocessData(dfRawData)
    rddBaskets = generateBaskets(dfPreprocessed)
    writeBaskets(rddBaskets)
    return rddBaskets

def loadTestDataInList():
    filepath = os.path.join(PROJECT_ROOT, 'data/processed/baskets.csv')
    baskets = list()
    with open(filepath, 'r') as file:
        for line in file:
            baskets.append([int(basketItem) for basketItem in line.split(',')])
    return baskets
#
# def loadTestDataInRDD(sparkSession: SparkSession):
#     dfRawData = sparkSession.read.csv(inputFilePath, header=True, schema=rawDataSchema, quote='"')


