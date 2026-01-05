import requests
import pandas as pd

API_KEY = "4a2ca042b8b2510f05d180b106799df5"

def extract_data(cities):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    records = []

    for city in cities:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(base_url, params=params)
        data = response.json()

        record = {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "weather": data["weather"][0]["description"],
            "timestamp": pd.to_datetime("now")
        }
        records.append(record)

    df = pd.DataFrame(records)
    return df
