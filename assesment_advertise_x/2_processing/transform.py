from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("DataTransformation").getOrCreate()

def transform_data(df):
    # Add any transformation logic here
    df = df.withColumn("timestamp", col("timestamp").cast("timestamp"))
    return df
