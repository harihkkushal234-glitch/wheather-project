from extract import extract_data
from transform import transform_data
from load import load_data

def run_etl():
    cities = ["Bengaluru", "Mumbai", "Delhi", "Chennai", "Kolkata" , "Ramanagara"]

    print("🔹 Extracting data...")
    raw_df = extract_data(cities)

    print("🔹 Transforming data...")
    clean_df = transform_data(raw_df)

    print("🔹 Loading data into database...")
    load_data(clean_df)

    print("✅ ETL process completed successfully!")

if __name__ == "__main__":
    run_etl()
