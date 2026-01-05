import pandas as pd

def transform_data(df):
    # Rename columns for clarity
    df.columns = ["city", "temperature_c", "humidity_pct", "wind_speed_mps", "weather_desc", "timestamp"]

    # Handle missing values
    df = df.fillna({"temperature_c": 0, "humidity_pct": 0, "wind_speed_mps": 0, "weather_desc": "unknown"})

    # Round numeric values
    df["temperature_c"] = df["temperature_c"].round(2)
    df["humidity_pct"] = df["humidity_pct"].round(2)
    df["wind_speed_mps"] = df["wind_speed_mps"].round(2)

    return df
