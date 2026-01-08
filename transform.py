def transform_state_data(df):
    # Round numeric values
    df["temperature_c"] = df["temperature_c"].round(2)
    df["humidity_pct"] = df["humidity_pct"].round(2)
    df["wind_speed_mps"] = df["wind_speed_mps"].round(2)

    # Create state-level summary (average values)
    state_summary = df.groupby("state").agg({
        "temperature_c": "mean",
        "humidity_pct": "mean",
        "wind_speed_mps": "mean"
    }).reset_index()

    return df, state_summary
