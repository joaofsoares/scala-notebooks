"""
PySpark - Word Counter

Execute: spark-submit.cmd --master="local[*]" script_directory/word_counter.py

"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import desc
import re


def is_non_empty(s: str) -> bool:
    return True if s else False


def clean_str(s: str) -> str:
    return "".join(filter(lambda c: c.isalnum(), s))


spark = SparkSession.builder.appName("Word Counter").getOrCreate()

df = spark.read.option("inferSchema", "true").format("text")\
    .load("file_path")

m_df = df.rdd.flatMap(lambda row : re.split("\W+", row[0]))\
    .map(lambda w: clean_str(w))\
    .filter(lambda w: is_non_empty(w))\
    .map(lambda w: (w, 1))\
    .toDF(["word", "count"]).cache()


m_df.groupBy("word").count().orderBy(desc("count")).show()

spark.stop()
