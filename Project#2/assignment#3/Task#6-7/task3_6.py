from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col

spark = SparkSession.builder.appName("Most_Popular_Superhero").getOrCreate()

lines = spark.read.option("inferSchema", "true").text("Marvel+Graph")
names = spark.read.option("inferSchema", "true").text("Marvel+Names")

#split lines into words
id_superhero = lines.select(explode(split(col("value"), " ")).alias("id_superhero"))

#split names into id and superhero name (each line has the format: id superhero_name)
superheros = names.select(split(col("value"), " ")[0].alias("id_superhero"), split(col("value"), " ",2)[1].alias("superhero_name"))

#count the frequency of each superhero
frequency = id_superhero.groupBy("id_superhero").count()

#join frequency with superheros to get the superhero name
frequency_with_names = frequency.join(superheros, "id_superhero")

#sort by frequency
frequency_with_names = frequency_with_names.sort(frequency_with_names["count"].desc())


#print the most popular superhero and its frequency, if there are more than one superhero with the same frequency, print them all
most_popular_frequency = frequency_with_names.first()[1]
most_popular_superheroes = frequency_with_names.filter(frequency_with_names["count"] == most_popular_frequency).collect()

for superhero in most_popular_superheroes:
    print("\nMost Popular Superhero: {1} \nFrequency: {0}\n".format(superhero[1], superhero[2]))


spark.sparkContext.setLogLevel("WARN")
spark.stop()