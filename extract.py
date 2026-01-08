import requests
import pandas as pd

API_KEY = "4a2ca042b8b2510f05d180b106799df5"

# Define states and representative cities
STATE_TO_CITIES = {
    "Karnataka": ["Bengaluru", "Mysuru", "Mangalore"],
    "Madhya Pradesh": ["Bhopal", "Indore", "Gwalior"],
    "Uttar Pradesh": ["Lucknow", "Kanpur", "Varanasi"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai"],
    "West Bengal": ["Kolkata", "Darjeeling", "Siliguri"]
}

def extract_state_data():
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    records = []

    for state, cities in STATE_TO_CITIES.items():
        for city in cities:
            params = {"q": city, "appid": API_KEY, "units": "metric"}
            response = requests.get(base_url, params=params)
            data = response.json()

            record = {
                "state": state,
                "city": city,
                "temperature_c": data["main"]["temp"],
                "humidity_pct": data["main"]["humidity"],
                "wind_speed_mps": data["wind"]["speed"],
                "weather_desc": data["weather"][0]["description"],
                "timestamp": pd.to_datetime("now")
            }
            records.append(record)

    return pd.DataFrame(records)
