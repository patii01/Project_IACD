from pyspark.sql import SparkSession

from pyspark.sql.functions import split, explode

# Create a Spark session
spark = SparkSession.builder.appName("WordFrequencyStreaming").getOrCreate()

# Set up a streaming source using the socket format
lines = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()

# Split the lines into words
words = lines.select(explode(split(lines.value, " ")).alias("word"))

# Count the number of occurrences of each word
wordCounts = words.groupBy("word").count()

words_sort = wordCounts.orderBy("count", ascending=True)

# Start running the query that prints the running counts to the console
query = words_sort.writeStream.outputMode("complete").format("console").start()

# Wait for the termination signal
query.awaitTermination()

# Stop the session
spark.sparkContext.setLogLevel("WARN")
spark.stop()


