import sqlite3

def load_state_data(city_df, state_df, db_name="weather_data.db", replace=False):
    conn = sqlite3.connect(db_name)

    mode = "replace" if replace else "append"

    # Save raw city-level data
    city_df.to_sql("weather_city", conn, if_exists=mode, index=False)

    # Save aggregated state-level data
    state_df.to_sql("weather_state", conn, if_exists=mode, index=False)

    conn.close()
    print(f"✅ Data saved to {db_name} (tables: weather_city, weather_state)")
