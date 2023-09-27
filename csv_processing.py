%spark.pyspark
from pyspark import SparkFiles
from pyspark.sql.types import StructType, StructField, StringType, IntegerType ,DoubleType
data_file_https_url = "https://raw.githubusercontent.com/davidmungai/spark_jobs/main/data/stock_data.csv"

# Open,High,Low,Close,Adj_Close,Volume
schema =  StructType([
      StructField("Open",DoubleType(),True),
      StructField("High",DoubleType(),True),
      StructField("Low",DoubleType(),True),
      StructField("Close",DoubleType(),True),
      StructField("Adj_Close",DoubleType(),True),
     StructField("Volume",IntegerType(),True)
])
sc.addFile(data_file_https_url)
df = spark.read.schema(schema).csv("file://" + SparkFiles.get("stock_data.csv"))
df.show()
df.filter("Close < 500").show()
type(df['open'])
df.createOrReplaceTempView('stock_data')
df.filter((df['close']<200) & (df['open']>200)).show()
