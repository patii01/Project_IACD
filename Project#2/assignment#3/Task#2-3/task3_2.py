from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col, regexp_replace, lower

spark = SparkSession.builder.appName("Obtain_Word_Frequency_Book").getOrCreate()

lines = spark.read.option("inferSchema", "true").text("Book")

# Replace non-alphanumeric characters with spaces
cleaned_lines = lines.withColumn("cleaned_text", lower(regexp_replace(col("value"), "[^a-zA-Z0-9_]+", " ")))

# Split lines into words
words = cleaned_lines.select(explode(split(col("cleaned_text"), " ")).alias("word"))

# Filter out empty words
words = words.filter(words.word != "")

# Count the frequency of each word
words = words.groupBy("word").count()

words.show()

spark.sparkContext.setLogLevel("WARN")
spark.stop()