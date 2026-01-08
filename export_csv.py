import sqlite3
import pandas as pd

def export_to_csv(db_name="weather_data.db", table_name="weather_state", csv_name="weather_state.csv"):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)

    # Read the table into a DataFrame
    df = pd.read_sql(f"SELECT * FROM {table_name};", conn)

    # Export to CSV
    df.to_csv(csv_name, index=False)

    conn.close()
    print(f"✅ Exported {table_name} to {csv_name}")

if __name__ == "__main__":
    export_to_csv()
