from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local").setAppName("Minimum_Temperature_Per_Capital")
sc = SparkContext(conf=conf)

lines = sc.textFile("1800.csv")

weather_data = lines.map(lambda x: (x.split(",")[0], x.split(",")[2], x.split(",")[3])) 
#(Weather Station, Observation Type, Temperature*10)

weather_data = weather_data.filter(lambda x: "TMIN" in x[1])
#(Weather Station, Temperature*10) -> filtrar por TMIN

weather_data = weather_data.map(lambda x: (x[0], int(x[2])))
#(Weather Station, Temperature) -> convertir a int

weather_data = weather_data.reduceByKey(lambda x, y: min(x, y))
#(Weather Station, Minimum Temperature) -> reduzir por minimo

for result in weather_data.collect():
    print(result[0] + "\t{0}°C".format(result[1]))