from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

print("Starting ETL pipeline...")

print("Extracting data...")
df = extract_data("data/raw/train.csv")

print("Transforming data...")
df_clean = transform_data(df)

print("Loading data...")
load_data(df_clean, "data/processed/cleaned_nyc_taxi.parquet")

print("ETL pipeline completed successfully")