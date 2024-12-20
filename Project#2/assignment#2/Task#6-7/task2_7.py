from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local").setAppName("Least_Popular_Superhero")
sc = SparkContext(conf=conf)

lines = sc.textFile("Marvel+Graph")
names = sc.textFile("Marvel+Names")

#marvel_names = names.map(lambda x: (int(x.split(" ")[0]), ' '.join(x.split(" ")[1:])))
marvel_names = names.map(lambda x: (int(x.split(" ")[0]), ' '.join([word.replace('"', '') for word in x.split(" ")[1:]])))

marvel_graphs = lines.flatMap(lambda x: x.split())

frequency = marvel_graphs.map(lambda x: (int(x), 1))
frequency = frequency.reduceByKey(lambda x, y: x + y)

#for each id in marvel_graphs, get the name from marvel_names
frequency_with_names = frequency.join(marvel_names)

marvel = frequency_with_names.map(lambda x: (x[1][0], x[1][1]))

marvel = marvel.sortByKey()

# Get the least popular frequency
least_popular_frequency = marvel.first()[0]

# Filter superheroes with the same frequency as the least popular one
least_popular_superheroes = marvel.filter(lambda x: x[0] == least_popular_frequency).collect()


for superhero in least_popular_superheroes:
    print("\nLeast Popular Superhero: {1} \nFrequency: {0}".format(superhero[0], superhero[1]))