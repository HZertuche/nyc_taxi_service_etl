from pyspark.sql import SparkSession
from pyspark.sql.functions import hour, dayofweek
from pyspark.sql.functions import col

# Create spark session
spark = SparkSession.builder \
    .appName("NY Taxi ETL") \
    .getOrCreate()
print("Spark session started")

# Read CSV
df = spark.read.csv(
    "data/raw/train.csv",
    header=True,
    inferSchema=True
)

print("Data loaded")

# Convert timestamps
df = df.withColumn("pickup_hour", hour(col("pickup_datetime")))
df = df.withColumn("pickup_weekday", dayofweek(col("pickup_datetime")))

# Filter valid coordinates from NYC
df = df.filter(
    (col("pickup_longitude") > -74.05) &
    (col("pickup_longitude") < -73.75)
)

print("Transformations applied")

# Save in Parquet format
df.write.mode("overwrite").parquet("data/processed/spark_taxi.parquet")

print("Spark ETL completed")