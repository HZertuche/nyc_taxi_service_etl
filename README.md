# NYC Taxi ETL Pipeline
End-to-end data engineering pipeline to process and analyze New York City taxi trip patterns.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PySpark](https://img.shields.io/badge/PySpark-ETL-orange)
![DuckDB](https://img.shields.io/badge/DuckDB-SQL-green)
![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)
![Parquet](https://img.shields.io/badge/Storage-Parquet-lightgrey)

## Table of Contents
- [Project Highlights](#project-highlights)
- [Project Overview](#project-overview)
- [Objective](#objective)
- [Dataset Source](#dataset-source)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [Architecture Diagram](#architecture-diagram)
- [Data Preprocessing](#data-preprocessing)
- [Running the Pipeline](#running-the-pipeline)
- [Data Quality Validation](#data-quality-validation)
- [How to Run](#how-to-run)
- [Example SQL Query](#example-sql-query)
- [PySpark Pipeline](#pyspark-pipeline)
- [Dashboard](#dashboard)
- [Key Insights](#key-insights)
- [Business Impact](#business-impact)
- [Assumptions and Limitations](#assumptions-and-limitations)
- [Future Improvements](#future-improvements)

## Project Highlights

- Built an end-to-end ETL pipeline to process New York City taxi trip data.
- Transformed raw CSV datasets into optimized Parquet files for analytical workloads.
- Implemented data validation checks to ensure dataset consistency.
- Generated analytical features such as trip distance and temporal patterns.
- Queried the processed data using DuckDB.
- Built an interactive Power BI dashboard to analyze urban mobility patterns.

## Project Overview

This project implements a complete ETL pipeline using the New York City Taxi Trip dataset.

The pipeline extracts raw trip data, performs data cleaning and feature engineering, filters invalid records, and stores optimized results in Parquet format for efficient analytics.The curated dataset is then queried using DuckDB and visualized through an interactive Power BI dashboard to analyze trip duration, demand patterns, and urban mobility behavior.

## Objective 

The goal of this project is to demonstrate core data engineering practices, including:

- Data cleaning
- Feature engineering
- Columnar storage using Parquet
- SQL analytics with DuckDB
- Data visualization using Power BI

## Dataset Source
This project uses the **2016 NYC Yellow Cab trip record data**, a public dataset commonly used for analytics and data engineering projects.

- **Source:** [Kaggle - New York City Taxi Trip Duration](https://www.kaggle.com/competitions/nyc-taxi-trip-duration/data)
- **Usage:** Educational and portfolio purposes only

> **Note:** This dataset is a sample of historical New York City taxi trips and does not represent full production data.

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
- **Python** – Data processing and pipeline scripting
- **DuckDB** – Local analytical SQL engine
- **Pandas / NumPy** – Data manipulation
- **Haversine** - Distance calculation
- **Parquet** - Columnar storage format optimized for analytics
- **Matplotlib / Seaborn** – Exploratory data analysis (EDA)
- **Power BI** - Data visualization and dashboarding
- **PySpark** - Distributed ETL processing

## Project Architecture

Extract → Transform → Load

Raw CSV → Data Cleaning → Feature Engineering → Parquet Storage → SQL Analytics → Power BI Dashboard

## Architecture Diagram
        Raw Data (CSV Files)
               │
               ▼
          Extract Layer
               │
               ▼
        Transform Layer
  (Data Cleaning + Feature Engineering)
               │
               ▼
           Load Layer
        Parquet Storage
               │
               ▼
         Analytics Layer
        DuckDB / Python
               │
               ▼
      Power BI Dashboard



## Data Preprocessing
Steps performed in the project:

1. Extracted raw taxi trip data from CSV files. 
2. Selected analytical columns relevant for trip duration and mobility analysis.
3. Cleaned and standarized timestamp fiels for pickup and dropoff times.
4. Filtered invalid geographic coordinates and removed outliers in trip duration.
5. Generated additional features such as trip distance, hour of day, and day of week.
6. Exported curated outputs in Parquet format for query performance optimization.

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

## PySpark Pipeline

The ETL pipeline was implemented using PySpark to handle data transformation at scale.

Key steps include:

- Data ingestion from raw CSV files
- Data cleaning and filtering
- Feature engineering (trip distance, time-based features)
- Aggregations and transformations
- Writing optimized outputs in Parquet format

## Data Quality Validation

During the transformation stage, several validation checks were applied:

- Ensured that critical fields do not contain null values.
- Validated data types for selected fields.
- Validation of datetime fields
- Removal of invalid geographic coordinates
- Detection of trips with zero distance
- Removal of extreme outliers in trip duration

## How to Run
1. Download the NYC Taxi trip duration dataset from Kaggle.
2. Place the raw CSV files in the appropriate folders within your local environment.
3. Run the main ETL script to extract, transform, and load the dataset.
4. Store the final output in Parquet format.
5. Query the curated dataset using DuckDB.
6. Connect the final dataset to Power BI to build the dashboard.

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

## Dashboard

### Main Dashboard
![Main Dashboard](screenshots/main_dashboard.PNG)

| Big Numbers | Map Pickups |
|-------------|-------------|
| ![](screenshots/big_numbers.PNG) | ![](screenshots/map_pickup.png) |

| Trips by Day | Trips by Hour |
|--------------|--------------|
| ![](screenshots/total_trips_per_day.PNG) | ![](screenshots/total_trips_per_hour.PNG) |

| Average Duration and Distance |
|--------------------------------|
| ![](screenshots/big_numbers_pt2.PNG) |

## Key Insights

- Midtown Manhattan shows the highest taxi pickup demand, indicating it is a major transportation hub within New York City.
- Most taxi trips occurs during eveneing hours, between 6:00 PM and 11:00 PM, suggesting increased mobility after trypical working hours.
- The average taxi trip duration is approximately 16 minutes, reflecting short-distance irban travel.
- Airports such as JFK and LaGuardia serve as key pickup and dropoff locations, highlighting their importance in city-wide transportation flows.
- Trip demand is concentrated in high-density urban areas, particularly in central Manhattan, where commercial and business activity is highest.
- Short and medium-distance trips dominate the dataset, suggesting that taxis are primarily used for convenience rather than long-distance travel.

## Business Impact

- **Operational planning:** Since trip demand peaks durign specific hours of the day, taxi and ride-hailing services can allocate more drivers during high-demand periods to reduce wait times and improve service efficiency.
- **Driver allocation**: Identifyiung high-demand zones and peak days of the week allows companies to strategically position drivers in areas with higher trip activity, increasing ride frequency and revenue per driver.
- **Route optimization**: Understanding trip duration patterns and traffic congestion trends, enables better route planning, helping reduce travel time, fuel consumption and operational costs.
- **Demand forecasting**: Historical trip patterns by hour and day can be used to predict future demand, supporting better scheduling and dynamic pricing strategies.
- **Customer experience**: By minimizing delays and improving trip time estimates, companies can enhance rider satisfaction and increase customer retention.

## Assumptions and Limitations

- This dataset is a public sample and does not represent full NYC taxi trip production data.
- The analysis is based on historical trip and should be interpreted as exploratory.
- The project focuses on batch ETL and analytical reporting rather than real-time processing.
- Business insights are inferred from trip duration, distance, and pickup/dropoff patterns, not from revenue or operational cost data.

## Future Improvements

- Migrate the ETL pipeline to a cloud-based orchestration service such as AWS Step Functions.
- Add data partitioning strategies to improve query performance in DuckDB and downstream analytics.
- Integrate data quality monitoring and validation frameworks.
- Deploy dashboards with scheduled refresh workflows.