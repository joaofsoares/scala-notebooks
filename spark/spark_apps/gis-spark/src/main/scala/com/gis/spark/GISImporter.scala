package com.gis.spark

import org.apache.log4j.{Level, Logger}
import org.apache.spark.sql.SparkSession

object GISImporter extends App {

  Logger.getLogger("org").setLevel(Level.ERROR)

  val spark = SparkSession.builder.appName("GIS Importer").master("local[*]").getOrCreate()

  val dataFrame = spark.read.option("inferSchema", "true").option("header", "true")
    .json("files/gis_san_francisco.json")

  import org.apache.spark.sql.functions._

  dataFrame.select(col("properties.BLKLOT"), col("properties.BLOCK_NUM"),
    col("properties.FROM_ST"), col("properties.LOT_NUM"),
    col("properties.MAPBLKLOT"), col("properties.ODD_EVEN"),
    col("properties.STREET"), col("properties.ST_TYPE"),
    col("properties.TO_ST"), col("type"), col("geometry.type"),
    explode(col("geometry.coordinates"))).show()

  spark.stop()


}
