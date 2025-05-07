import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_current_weather(lat, lon):
    api_key = os.getenv("OPENWEATHER_KEY")
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric",
        "lang": "kr"
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return None
    data = response.json()
    return data["weather"][0]["main"]  # "Clear", "Rain", etc.
