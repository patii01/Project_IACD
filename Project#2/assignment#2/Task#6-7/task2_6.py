from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local").setAppName("Most_Popular_Superhero")
sc = SparkContext(conf=conf)

lines = sc.textFile("Marvel+Graph")
names = sc.textFile("Marvel+Names")

marvel_names = names.map(lambda x: (int(x.split(" ")[0]), ' '.join([word.replace('"', '') for word in x.split(" ")[1:]])))

marvel_graphs = lines.flatMap(lambda x: x.split())

frequency = marvel_graphs.map(lambda x: (int(x), 1))
frequency = frequency.reduceByKey(lambda x, y: x + y)

#for each id in marvel_graphs, get the name from marvel_names
frequency_with_names = frequency.join(marvel_names)

marvel = frequency_with_names.map(lambda x: (x[1][0], x[1][1]))

marvel = marvel.sortByKey(False)

# Get the most popular frequency
most_popular_frequency = marvel.first()[0]

# Filter superheroes with the same frequency as the most popular one
most_popular_superheroes = marvel.filter(lambda x: x[0] == most_popular_frequency).collect()

for superhero in most_popular_superheroes:
    print("\n\nMost Popular Superhero: {1} \nFrequency: {0}\n\n".format(superhero[0], superhero[1]))
