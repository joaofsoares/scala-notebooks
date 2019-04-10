name := "gis-spark"

version := "0.1"

scalaVersion := "2.12.8"

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-sql" % "2.4.1",
  "org.apache.logging.log4j" % "log4j-core" % "2.11.2")
