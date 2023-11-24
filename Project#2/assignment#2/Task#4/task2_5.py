from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local").setAppName("Sort_Total_Amount_Spent_Customer")
sc = SparkContext(conf=conf)

lines = sc.textFile("customer-orders.csv")

customer_data = lines.map(lambda x: (x.split(",")[0], x.split(",")[2]))
#(Customer ID, Amount) 

customer_data = customer_data.map(lambda x: (x[0], float(x[1])))

customer_data = customer_data.reduceByKey(lambda x, y: x + y)

customer_data = customer_data.map(lambda x: (x[1], x[0]))

customer_data = customer_data.sortByKey(False)

for result in customer_data.collect():
    print(result[1] + "\t{:.3f}".format(result[0]))
