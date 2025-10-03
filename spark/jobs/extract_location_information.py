from pyspark.sql import SparkSession
from pyspark.sql.functions import split, regexp_extract, udf
from pyspark.sql.types import StringType
import re

spark = SparkSession.builder.appName("TransformAddresses").getOrCreate()

# Reading from postgres
df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/postgres") \
    .option("dbtable", "customers") \
    .option("user", "postgres") \
    .option("password", "postgres") \
    .load()

# Extracts first digit of postcode from address
def extract_postcode(address):
    match = re.search(r"\b\d{5}\b", address)
    return match.group(0)[0] if match else None

extract_postcode_udf = udf(extract_postcode, StringType())
df = df.withColumn("postcode_first_digit", extract_postcode_udf(df["address"]))

mapping_df = spark.read.csv("/app/mapping.csv", header=True, sep=";")
mapping_df = mapping_df.select("PLZ_erstes_zeichen", "Bundesland")

result_df = df.join(mapping_df, df.postcode_first_digit == mapping_df.PLZ_erstes_zeichen, "left").select(df["*"], mapping_df.Bundesland.alias("Bundesland"))

result_df.show(truncate=False)

# Write back to postgres
result_df.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/postgres") \
    .option("dbtable", "customers_complete") \
    .option("user", "postgres") \
    .option("password", "postgres") \
    .mode("overwrite") \
    .save()