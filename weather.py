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

    print("[DEBUG] 날씨 응답 코드:", response.status_code)
    print("[DEBUG] 날씨 응답 내용:", response.text[:200])

    if response.status_code != 200:
        return None
    data = response.json()
    return data["weather"][0]["main"]  # "Clear", "Rain", etc.

def get_weather_display_text(weather_main):
    mapping = {
        "Clear": "☀️ 맑음",
        "Clouds": "☁️ 흐림",
        "Rain": "🌧️ 비",
        "Snow": "❄️ 눈",
        "Thunderstorm": "⛈️ 천둥번개",
        "Drizzle": "🌦️ 이슬비",
        "Mist": "🌫️ 안개",
        "Haze": "🌁 연무",
        "Dust": "🌪️ 황사",
        "Fog": "🌁 안개",
        "Squall": "💨 돌풍",
        "Tornado": "🌪️ 토네이도"
    }
    
    return mapping.get(weather_main, f"🌈 {weather_main}")
