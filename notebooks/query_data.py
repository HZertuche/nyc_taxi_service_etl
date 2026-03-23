import duckdb

df = duckdb.query("""
SELECT 
    weekday,
    AVG(distance_km) as avg_distance
FROM 'data/processed/cleaned_nyc_taxi.parquet'
GROUP BY weekday
""").df()

print(df)