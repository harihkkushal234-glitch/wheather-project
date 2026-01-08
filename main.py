from extract import extract_state_data
from transform import transform_state_data
from load import load_state_data

def run_etl():
    print("🔹 Extracting data...")
    raw_df = extract_state_data()

    print("🔹 Transforming data...")
    city_df, state_df = transform_state_data(raw_df)

    print("🔹 Loading data into database...")
    load_state_data(city_df, state_df)

    print("✅ ETL process completed successfully!")

if __name__ == "__main__":
    run_etl()
