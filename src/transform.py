
import pandas as pd
from haversine import haversine_vector, Unit

def transform_data(df):
    
    #Convert dates
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
    df['dropoff_datetime'] = pd.to_datetime(df['dropoff_datetime'])

    # Filter valid coordinates from NYC
    df = df[(df['pickup_longitude'].between(-74.05, -73.75)) &
            (df['pickup_latitude'].between(40.63, 40.85))]

    # Feature engineering
    df['distance_km'] = haversine_vector(
    df[['pickup_latitude', 'pickup_longitude']].to_numpy(),
    df[['dropoff_latitude', 'dropoff_longitude']].to_numpy(),
    unit=Unit.KILOMETERS
    )
    # Hour and day of the week
    df['hour'] = df['pickup_datetime'].dt.hour
    df['weekday'] = df['pickup_datetime'].dt.weekday

    return df