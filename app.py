import os
import requests

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from config import SERVICE_KEY, OPENWEATHER_KEY
from location_coords import location_coords
from weather import get_current_weather, get_weather_display_text
from filter import filter_places_by_weather
from recommender.recommend_model import (
    get_hotel_recommendations,
    get_restaurant_recommendations
)
from translatepy import Translator
from translations import translate_city_name, translate_district_name

translator = Translator()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

CATEGORY_CODE_MAP = {
    "음식점": "39",
    "숙소": "32",
    "관광지": "12",
    "쇼핑": "38",
}

@app.get("/", response_class=HTMLResponse)
async def select_language(request: Request):
    return templates.TemplateResponse("select_language.html", {"request": request})

@app.get("/select_category", response_class=HTMLResponse)
async def select_category(request: Request, language: str = "Korean"):
    return templates.TemplateResponse("select_category.html", {
        "request": request,
        "language": language
    })

@app.post("/select_region", response_class=HTMLResponse)
async def select_region(request: Request, language: str = Form(...)):
    return templates.TemplateResponse("select_region.html", {
        "request": request,
        "language": language
    })

@app.post("/show_recommendations", response_class=HTMLResponse)
async def show_recommendations(
    request: Request,
    category: str = Form(...),
    city: str = Form(...),
    district: str = Form(...),
    city_name: str = Form(...),
    district_name: str = Form(...),
    language: str = Form(...)
):
    area_data = await get_area_code(city, district)
    if not area_data:
        return templates.TemplateResponse("recommendations.html", {
            "request": request,
            "category": category,
            "city": city,
            "district": district,
            "city_name": city_name,
            "district_name": district_name,
            "places": [],
            "weather": None,
            "weather_display": None,
            "language": language,
            "error": "지역 정보를 찾을 수 없습니다."
        })

    area_code, sigungu_code = area_data
    places = await get_api_recommendations(category, area_code, sigungu_code)
    original_places = places.copy()

    if language != "Korean":
        for place in places:
            for field in ["title", "addr", "openTime"]:
                if place.get(field):
                    try:
                        translated = translator.translate(place[field], language)
                        place[field] = translated.result
                    except:
                        print(f"[WARN] 번역 실패: {place[field]}")

    weather = None
    weather_display = None
    if category == "관광지":
        coords = location_coords.get(city)
        if coords:
            lat, lon = coords
            weather = get_current_weather(lat, lon)
            weather_display = get_weather_display_text(weather)
            if weather:
                places = filter_places_by_weather(original_places, weather)
                if not places:
                    places = original_places
        if language != "Korean" and weather:
            try:
                weather = translator.translate(weather, language).result
            except:
                print("[WARN] 날씨 번역 실패")

    return templates.TemplateResponse("recommendations.html", {
        "request": request,
        "category": category,
        "city": city,
        "district": district,
        "city_name": city_name,
        "district_name": district_name,
        "places": places,
        "weather": weather,
        "weather_display": weather_display,
        "language": language,
        "error": None
    })

@app.post("/select_category", response_class=HTMLResponse)
async def select_category(
    request: Request,
    language: str = Form(...),
    category: str = Form(...),
    city: str = Form(...),
    district: str = Form(...),
    city_name: str = Form(...),
    district_name: str = Form(...)
):
    return templates.TemplateResponse("select_category.html", {
        "request": request,
        "language": language,
        "city": city,
        "district": district,
        "city_name": city_name,
        "district_name": district_name
    })

@app.get("/get_cities", response_class=JSONResponse)
async def get_cities(language: str = "Korean"):
    url = f"http://apis.data.go.kr/B551011/KorService1/areaCode1?serviceKey={SERVICE_KEY}"
    params = {
        "MobileOS": "ETC",
        "MobileApp": "AppTest",
        "_type": "json",
        "numOfRows": 100
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return JSONResponse(content={"error": "Failed to fetch cities"}, status_code=500)
    try:
        data = response.json()
    except:
        return JSONResponse(content={"error": "Invalid JSON response"}, status_code=500)
    items = data.get("response", {}).get("body", {}).get("items", {}).get("item", [])
    cities = []
    for item in items:
        name = item["name"]
        code = item["code"]
        translated_name = translate_city_name(name, language)
        if not translated_name and language != "Korean":
            try:
                translated_name = translator.translate(name, language).result
            except:
                translated_name = name
        cities.append({"name": translated_name or name, "code": code})
    return JSONResponse(content={"cities": cities})

@app.get("/get_districts", response_class=JSONResponse)
async def get_districts(area_code: int, language: str = "Korean"):
    url = f"http://apis.data.go.kr/B551011/KorService1/areaCode1?serviceKey={SERVICE_KEY}&areaCode={area_code}&MobileOS=ETC&MobileApp=AppTest&_type=json&numOfRows=100"
    response = requests.get(url)
    if response.status_code != 200:
        return JSONResponse(content={"error": "Failed to fetch districts"}, status_code=500)
    try:
        data = response.json()
    except:
        return JSONResponse(content={"error": "Invalid JSON"}, status_code=500)
    items = data.get("response", {}).get("body", {}).get("items", {}).get("item", [])
    districts = []
    for item in items:
        name = item["name"]
        code = item["code"]
        translated_name = translate_district_name(name, language)
        if not translated_name and language != "Korean":
            try:
                translated_name = translator.translate(name, language).result
            except:
                translated_name = name
        districts.append({"name": translated_name or name, "code": code})
    return JSONResponse(content=districts)

async def get_area_code(city_code: str, district_code: str):
    return int(city_code), int(district_code)

async def get_api_recommendations(category: str, area_code: str, sigungu_code: str):
    content_type_id = CATEGORY_CODE_MAP.get(category)
    if not content_type_id:
        return []
    url = f"http://apis.data.go.kr/B551011/KorService1/areaBasedList1?serviceKey={SERVICE_KEY}"
    params = {
        "MobileOS": "ETC",
        "MobileApp": "KoreaTripMate",
        "_type": "json",
        "areaCode": area_code,
        "sigunguCode": sigungu_code,
        "contentTypeId": content_type_id,
        "numOfRows": 12
    }
    if content_type_id == "12":
        params["listYN"] = "Y"
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return []
    try:
        data = response.json()
        if isinstance(data, str):
            import json
            data = json.loads(data)
    except:
        return []
    items = data.get("response", {}).get("body", {}).get("items", {}).get("item", [])
    results = []
    for item in items:
        results.append({
            "title": item.get("title", "이름 없음"),
            "tel": item.get("tel", ""),
            "openTime": item.get("openTime", ""),
            "addr": item.get("addr1", ""),
            "map_addr": item.get("addr1", ""),
            "cat3": item.get("cat3", ""),
            "firstimage": item.get("firstimage", "")
        })
    return results