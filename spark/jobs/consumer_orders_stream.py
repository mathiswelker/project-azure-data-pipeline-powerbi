from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StringType, IntegerType, DoubleType, StructType
spark = SparkSession.builder.appName("consumer_orders_stream").getOrCreate()

# defining a schema
order_schema = StructType() \
    .add("order_id", StringType()) \
    .add("customer_id", IntegerType()) \
    .add("product_id", IntegerType()) \
    .add("price", DoubleType()) \
    .add("quantity", IntegerType()) \
    .add("order_date", StringType())

# Reading orders from kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "orders") \
    .load()

# Converts into json and accesses fields inside JSON
df_json = df.select(from_json(col("value").cast("string"), order_schema).alias("order"))
df_json = df_json.select("order.*")

# Calculate total_amount and remove price column
df_json = df_json.withColumn("total_amount", round(col("price") * col("quantity"), 2))
df_json = df_json.drop("price")


# Write back to postgres
df_json.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/postgres") \
    .option("dbtable", "customers_complete") \
    .option("user", "postgres") \
    .option("password", "postgres") \
    .mode("overwrite") \
    .save()