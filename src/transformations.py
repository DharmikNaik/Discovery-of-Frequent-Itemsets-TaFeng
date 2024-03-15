from pyspark.sql import DataFrame
from pyspark.sql.functions import concat, col, lit, regexp_replace, collect_set
from pyspark import RDD


def preprocessData(df: DataFrame) -> DataFrame:
    return df.select("TRANSACTION_DT", "CUSTOMER_ID", "PRODUCT_ID")\
        .withColumn("BASKET_ID", concat(col("TRANSACTION_DT"), lit("-"), col("CUSTOMER_ID"))) \
        .drop("TRANSACTION_DT", "CUSTOMER_ID") # droping columns to reclaim memory


def generateBaskets(df: DataFrame) -> RDD:
    return df.groupBy("BASKET_ID").agg(collect_set("PRODUCT_ID").alias("BASKET"))\
        .drop("BASKET_ID")\
        .rdd


def parseDfBasketsToList(partition):
    return [record.BASKET for record in list(partition)]