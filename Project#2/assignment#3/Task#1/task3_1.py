from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Minimum_Temperature_Per_Capital").getOrCreate()

lines = spark.read.option("inferSchema", "true").csv("1800.csv")

# Select only weatherStation, observationType and temperature
stationTemps = lines.select("_c0", "_c2", "_c3")

# Filter out all but TMIN entries
minTemps = stationTemps.filter(stationTemps._c2 == "TMIN")

# Select only stationID and temperature
stationTemps = minTemps.select("_c0", "_c3")

# Aggregate to find minimum temperature for every station
minTempsByStation = stationTemps.groupBy("_c0").min("_c3")

#Change name of header
minTempsByStation = minTempsByStation.withColumnRenamed("_c0", "WeatherStation").withColumnRenamed("min(_c3)", "MinTemperature")

minTempsByStation.show()

spark.sparkContext.setLogLevel("WARN")
spark.stop()

