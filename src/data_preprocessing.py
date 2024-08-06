from pyspark.sql import SparkSession

def preprocess_data(file_path):
    spark = SparkSession.builder.appName('AudioPreprocessing').getOrCreate()
    df = spark.read.csv(file_path, header=True)
    # Add preprocessing steps
    return df
