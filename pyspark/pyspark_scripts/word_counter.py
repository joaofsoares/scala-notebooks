"""
PySpark - Word Counter

Execute: spark-submit.cmd --master="local[*]" script_directory/word_counter.py

"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import desc
import re
import sys


def execute_spark(file_name):
    """
    Execute spark batch
    """
    def is_non_empty(s: str) -> bool:
        """
        Check if the string is not empty
        """
        return True if s else False


    def clean_str(s: str) -> str:
        """
        Clean special characters from the string
        """
        return "".join(filter(lambda c: c.isalnum(), s))


    spark = SparkSession.builder.appName("Word Counter").getOrCreate()

    df = spark.read.option("inferSchema", "true").format("text")\
        .load(file_name)

    m_df = df.rdd.flatMap(lambda row : re.split("\W+", row[0]))\
        .map(lambda w: clean_str(w))\
        .filter(lambda w: is_non_empty(w))\
        .map(lambda w: (w, 1))\
        .toDF(["word", "count"]).cache()


    m_df.groupBy("word").count().orderBy(desc("count")).show()

    spark.stop()


if __name__ == "__main__":
    execute_spark(sys.argv[1])