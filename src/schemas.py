
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, LongType, DoubleType

rawDataSchema = StructType([
    StructField("TRANSACTION_DT", StringType(), False),
    StructField("CUSTOMER_ID", LongType(), False),
    StructField("AGE_GROUP", StringType(), True),
    StructField("PIN_CODE", StringType(), True),
    StructField("PRODUCT_SUBCLASS", StringType(), True),
    StructField("PRODUCT_ID", LongType(), False),
    StructField("AMOUNT", StringType(), True),
    StructField("ASSET", StringType(), True),
    StructField("SALES_PRICE", StringType(), True),
])