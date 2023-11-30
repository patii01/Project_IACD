from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col

spark = SparkSession.builder.appName("Sort_Word_Frequency_Book").getOrCreate()

lines = spark.read.option("inferSchema", "true").text("Book")

# Split lines into words
words = lines.select(explode(split(col("value"), " ")).alias("word"))

# Filter out empty words
words = words.filter(words.word != "")

# Count the frequency of each word
words = words.groupBy("word").count()

# Sort the words by frequency
words = words.sort(words["count"].desc())

words.show()

spark.sparkContext.setLogLevel("WARN")
spark.stop()