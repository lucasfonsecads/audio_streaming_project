"""
Module for data preprocessing using PySpark.
"""

from pyspark.sql import SparkSession # type: ignore

def preprocess_data(file_path):
    """
    Preprocess the data from the given file path using PySpark.

    Args:
        file_path (str): Path to the input data file.

    Returns:
        DataFrame: Preprocessed data as a PySpark DataFrame.
    """
    spark = SparkSession.builder.appName('AudioPreprocessing').getOrCreate()
    return spark.read.csv(file_path, header=True)
