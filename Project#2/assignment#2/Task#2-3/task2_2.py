from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local").setAppName("Obtain_Word_Frequency_Book")
sc = SparkContext(conf=conf)

lines = sc.textFile("Book")

words = lines.flatMap(lambda x: x.split())
#split() -> separa por espaços em branco

words = words.map(lambda x: (x, 1))
#(word, 1) -> mapear para (word, 1), cada palavra aparece 1 vez

words = words.reduceByKey(lambda x, y: x + y)
#(word, frequency) -> reduzir por soma, sempre que aparecer x, soma 1

for result in words.collect():
    print("{0}\t".format(result[1]) + result[0])