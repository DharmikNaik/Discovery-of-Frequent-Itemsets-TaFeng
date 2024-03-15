from pyspark.sql import DataFrame
from src.constants import PROJECT_ROOT
import os

def outputDataframe(df: DataFrame, filepath: str, header=True):
    outputFilepath = os.path.join(PROJECT_ROOT, filepath)
    df.write.csv(outputFilepath, header=header)
def outputData(ls, config):
    outputFilepath = os.path.join(PROJECT_ROOT, config['file_paths']['output_path'])
    with open(outputFilepath, 'w') as file:
        for item in ls:
            file.write(f'{item}\n')

def writeBaskets(rdd):
    outputFilepath = os.path.join(PROJECT_ROOT, 'data/processed/baskets.csv')
    with open(outputFilepath, 'w') as file:
        for record in rdd.collect():
            basket = record.BASKET
            file.write(','.join(map(str, basket))+'\n')