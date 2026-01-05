import sqlite3
import pandas as pd

# Connect to your SQLite database
conn = sqlite3.connect("weather_data.db")

# Read the entire weather table into a DataFrame
df = pd.read_sql("SELECT * FROM weather;", conn)

# Export to CSV
df.to_csv("weather_data.csv", index=False)

# Close connection
conn.close()

print("✅ Data exported successfully to weather_data.csv")
