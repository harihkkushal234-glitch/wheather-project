import sqlite3

def load_data(df, db_name="weather_data.db"):
    conn = sqlite3.connect(db_name)
    df.to_sql("weather", conn, if_exists="append", index=False) #True for index Defult False
    conn.close()
