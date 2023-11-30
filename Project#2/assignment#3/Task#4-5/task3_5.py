from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col

spark = SparkSession.builder.appName("Sort_Total_Amount_Spent_Customer").getOrCreate()

lines = spark.read.option("inferSchema", "true").csv("customer-orders.csv")

# Select only customerID and amount
customerAmount = lines.select("_c0", "_c2")

# Aggregate to find total amount spent by every customer
totalAmountByCustomer = customerAmount.groupBy("_c0").sum("_c2")

#Sort the customers by total amount spent
totalAmountByCustomer = totalAmountByCustomer.sort(totalAmountByCustomer["sum(_c2)"].desc())

#Change name of header
totalAmountByCustomer = totalAmountByCustomer.withColumnRenamed("_c0", "CustomerID").withColumnRenamed("sum(_c2)", "TotalAmountSpent")

totalAmountByCustomer.show()

spark.sparkContext.setLogLevel("WARN")
spark.stop()