from delta import *
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataLoad").config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension").config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog").getOrCreate()

def load_data(df, path):
    df.write.format("delta").mode("overwrite").save(path)

# Example usage
data = [("abc123", "user456", "2024-05-25T12:34:56", "example.com")]
columns = ["ad_creative_id", "user_id", "timestamp", "website"]
df = spark.createDataFrame(data, columns)
load_data(df, "s3a://advertisex-data-bucket/ad_impressions")
