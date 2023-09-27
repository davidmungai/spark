%spark.pyspark
#this notebook was done in apatche zepellin
from pyspark import SparkFiles
#importing file from github url
data_file_https_url = "https://raw.githubusercontent.com/apache/spark/master/examples/src/main/resources/people.json"
#add file using pyspark sc.addfile functionality
sc.addFile(data_file_https_url)
#read json file
df = spark.read.json("file://" + SparkFiles.get("people.json"))
#show created dataframe
df.show()
#print dataframe schema
df.printSchema()
#show gotten file
df.columns
#describe gives a glimpe for the dataframe with stats like mean , deviation
df.describe().show()
#select a specific column
df.select("age").show()
#create a new column base off a another column
df_double=df.withColumn('doublage',df['age']*2)
#create a table from existing json
df.createOrReplaceTempView('people')
#running queries from the create table
result = spark.sql("select * from people")
#show gotten results
result.show()
