# NYC Taxi ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PySpark](https://img.shields.io/badge/PySpark-ETL-orange)
![DuckDB](https://img.shields.io/badge/DuckDB-SQL-green)
![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)
![Parquet](https://img.shields.io/badge/Storage-Parquet-lightgrey)


Data engineering pipeline built to process and analyze New York City taxi trip data.

## Project Overview

This project implements a complete ETL pipeline using the New York City Taxi Trip dataset.

The pipeline extracts raw trip data, performs data cleaning and feature engineering, and stores optimized results in Parquet format for efficient analytics.

## Objective 

The goal of this project is to demonstrate core data engineering practices, including:

- Data cleaning
- Feature engineering
- Columnar storage using Parquet
- SQL analytics with DuckDB
- Data visualization using Power BI

## Dataset
The dataset contains information about taxi travel time and distance in New York City. 

Key features include:
- *id* - Unique identifier for each trip
- *vendor_id* - Code indicating the provider associated with the trip record
- *pickup_datetime* - Date and time for client pickup 
- *dropoff_datetime* - Date and time for client dropoff
- *passenger_count* - Number of passengers
- *pickup_longitude* - Longitude coordinate for client pickup
- *pickup_latitude* - Latitude coordinate for client pickup
- *dropoff_longitude* - Longitude coordinate for client dropoff
- *dropoff_latitude* - Latitude coordinate for client dropoff
- *store_and_fwd_flag* - Y=store and forward (trip record in vehicle memory and send when connection is available); N=not a store and forward trip (real time)
- *trip_duration* - Trip duration in seconds

## Project Structure
```
nyc-taxi-service-etl
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── spark/
│   └── spark.pipeline.py
│
├── screenshots/
│
└── main.py
```

## Tech Stack
- Python
- Pandas / NumPy – Data manipulation
- Haversine - Distance calculation
- Parquet - Columnar Storage Format
- DuckDB - Query results
- Matplotlib / Seaborn – Exploratory Data Analysis (EDA)
- Power BI - Data visualization dashboard
- PySpark - Distributed ETL processing

## Project Architecture

Extract → Transform → Load

Raw CSV → Data Cleaning → Feature Engineering → Parquet Storage → SQL Analytics → Power BI Dashboard

## Architecture Diagram
           Raw Data
         (CSV Files)
               │
               ▼
          Extract Layer
               │
               ▼
        Transform Layer
    - Data Cleaning
    - Feature Engineering
               │
               ▼
           Load Layer
        Parquet Storage
               │
               ▼
         Analytics Layer
      (DuckDB / Python)
               │
               ▼
      Dashboard (Power BI)



## Pipeline Steps

### Extract
Load raw taxi trip data from CSV.

### Transform
- Clean timestamps
- Filter invalid geographic coordinates
- Remove outliers
- Generate new features:
  - Trip distance
  - Hour of day
  - Day of week

### Load
Store cleaned dataset in Parquet format for efficient analytics.

## Running the Pipeline

1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Run the pipeline:
```python
python main.py
```

## Data Quality Validation

During the transformation stage, several validation checks were applied:

- Removal of invalid geographic coordinates
- Detection of trips with zero distance
- Removal of extreme outliers in trip duration
- Validation of datetime fields


## Example SQL Query
Using DuckDB:

```sql
SELECT 
  weekday, 
  AVG(distance_km) as avg_distance
FROM cleaned_nyc_taxi.parquet
GROUP BY weekday
ORDER BY weekday;
```
## Business Impact

Analyzing NYC taxi trip data can help identify travel patterns and better understand urban mobility patterns.

Key insights may include:

- Peak taxi demand hours
- Average travel distances across weekdays
- Trip duration patterns during rush hours


## PySpark Pipeline

A scalable ETL pipeline was also implemented using PySpark.

Run with:

```bash
python spark/spark_pipeline.py
```

This pipeline demonstrates distributed data processing similar to production data engineering workflows.

## Dashboard

A Power BI dashboard was created to explore taxi trip patterns across New York City, including:

- Pickup hotspots
- Trips by day and hour
- Average trip duration and distance

### Main Dashboard
![Main Dashboard](screenshots/main_dashboard.png)

## Key Insights

- Midtown Manhattan is the area with the highest taxi pickup demand.
- Most taxi trips occur between 6 PM and 11 PM.
- The average taxi trip lasts around 16 minutes.
- Airports such as JFK and LaGuardia represent important pickup and dropoff hubs.

### Key Visualizations

| Big Numbers | Map Pickups |
|-------------|-------------|
| ![](screenshots/big_numbers.png) | ![](screenshots/map_pickup.png) |

| Trips by Day | Trips by Hour |
|--------------|--------------|
| ![](screenshots/total_trips_per_day.png) | ![](screenshots/total_trips_per_hour.png) |

| Average Duration and Distance |
|--------------------------------|
| ![](screenshots/big_numbers_pt2.png) |

