from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("DataCorrelation").getOrCreate()

def correlate_data(impressions_df, clicks_df):
    # Join impressions and clicks data
    correlated_df = impressions_df.join(clicks_df, ["user_id"], "inner")
    return correlated_df
