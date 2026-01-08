import sqlite3

def load_state_data(city_df, state_df, db_name="weather_data.db"):
    conn = sqlite3.connect(db_name)

    # Save raw city-level data
    city_df.to_sql("weather_city", conn, if_exists="append", index=False)

    # Save aggregated state-level data
    state_df.to_sql("weather_state", conn, if_exists="append", index=False)

    conn.close()
