import os
import requests

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from config import SERVICE_KEY,OPENWEATHER_KEY  # .env에서 API 키 불러오기

from location_coords import location_coords
from weather import get_current_weather, get_weather_display_text
from filter import filter_places_by_weather
from recommender.recommend_model import (
    get_hotel_recommendations,
    get_restaurant_recommendations
)
from translatepy import Translator

translator = Translator()

app = FastAPI()


# HTML 템플릿 폴더 설정
templates = Jinja2Templates(directory="templates")

# 카테고리에 맞는 한국관광공사 contentTypeId 매핑
CATEGORY_CODE_MAP = {
    "음식점": "39",    # 음식점
    "숙소": "32",      # 숙박
    "관광지": "12",    # 관광지
    "쇼핑": "38",      # 쇼핑
}

@app.get("/recommend/hotel")
async def recommend_hotel(user_id: int = 1):
    return {"recommendations": get_hotel_recommendations(user_id)}

@app.get("/recommend/restaurant")
async def recommend_restaurant(user_id: int = 1):
    return {"recommendations": get_restaurant_recommendations(user_id)}


# ▶ 1. 카테고리 선택 페이지
@app.get("/", response_class=HTMLResponse)
async def select_category(request: Request):
    return templates.TemplateResponse("select_category.html", {"request": request})

# ▶ 2. 지역 선택 페이지 (시/도, 시군구)
@app.post("/select_region", response_class=HTMLResponse)
async def select_region(request: Request, 
                        category: str = Form(...),
                        language: str = Form(...)
                        ):
    return templates.TemplateResponse("select_region.html", {
        "request": request, 
        "category": category,
        "language": language
        })

# ▶ 3. 최종 추천 결과 페이지
from translatepy import Translator
translator = Translator()

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
    # 지역 코드 얻기
    area_data = await get_area_code(city, district)
    if not area_data:
        return templates.TemplateResponse("recommendations.html", {
            "request": request,
            "category": category,
            "city": city_name,
            "district": district_name,
            "places": [],
            "weather": None,
            "weather_display": None,
            "language": language,
            "error": "지역 정보를 찾을 수 없습니다."
        })

    area_code, sigungu_code = area_data

    # 장소 추천 API 호출
    places = await get_api_recommendations(category, area_code, sigungu_code)

    original_places = places.copy()

    # 다국어 번역 (title, addr, openTime)
    if language != "Korean":
        for place in places:
            for field in ["title", "addr", "openTime"]:
                if place.get(field):
                    try:
                        translated = translator.translate(place[field], language)
                        place[field] = translated.result
                    except:
                        print(f"[WARN] 번역 실패: {place[field]}")

 

    # 날씨 기반 필터링 (관광지일 때)
    weather = None
    weather_display = None
    if category == "관광지":
        coords = location_coords.get(city)
        if coords:
            lat, lon = coords
            weather = get_current_weather(lat, lon)
            weather_display = get_weather_display_text(weather)
            print("[DEBUG] 현재 날씨:", weather)
            
            if weather:
                places = filter_places_by_weather(original_places, weather)

                #  필터링 후 아무것도 없으면 원래 추천 보여주기
                if not places:
                    print("[DEBUG] 날씨 조건에 맞는 장소 없음. 원본 추천을 사용합니다.")
                    places = original_places

        # 날씨도 번역 (옵션)
        if language != "Korean" and weather:
            try:
                weather = translator.translate(weather, language).result
            except:
                print("[WARN] 날씨 번역 실패")

    # 최종 추천 결과 렌더링
    return templates.TemplateResponse("recommendations.html", {
        "request": request,
        "category": category,
        "city": city_name,
        "district": district_name,
        "places": places,
        "weather": weather,
        "weather_display": weather_display,
        "language": language,
        "error": None
    })


# ▶ 4. (API) 시/도 리스트 가져오기
@app.get("/get_cities", response_class=JSONResponse)
async def get_cities():
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
    except Exception as e:
        return JSONResponse(content={"error": "Invalid JSON response"}, status_code=500)

    items = data.get("response", {}).get("body", {}).get("items", {}).get("item", [])
    cities = [{"name": item["name"], "code": item["code"]} for item in items]
    return JSONResponse(content={"cities": cities})

# ▶ 5. (API) 선택한 시/도에 대한 시군구 리스트 가져오기
@app.get("/get_districts", response_class=JSONResponse)
async def get_districts(area_code: int):
    #  areaCode는 URL에 직접 포함
    url = f"http://apis.data.go.kr/B551011/KorService1/areaCode1?serviceKey={SERVICE_KEY}&areaCode={area_code}&MobileOS=ETC&MobileApp=AppTest&_type=json&numOfRows=100"

    response = requests.get(url)
    

    if response.status_code != 200:
        return JSONResponse(content={"error": "Failed to fetch districts"}, status_code=500)

    try:
        data = response.json()
    except Exception as e:
        return JSONResponse(content={"error": "Invalid JSON"}, status_code=500)

    items = data.get("response", {}).get("body", {}).get("items", {}).get("item", [])
    districts = [{"name": item["name"], "code": item["code"]} for item in items]
    return JSONResponse(content=districts)


# 🔹 (보조 함수) 시/도 + 시군구 코드를 얻는 함수
async def get_area_code(city_code: str, district_code: str):
    print("[DEBUG] city_code:", city_code)
    print("[DEBUG] district_code:", district_code)
    return int(city_code), int(district_code)


    url = f"http://apis.data.go.kr/B551011/KorService1/areaCode1?serviceKey={SERVICE_KEY}"
    params = {
        "MobileOS": "ETC",
        "MobileApp": "AppTest",
        "_type": "json",
        "numOfRows": 100
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return None

    data = response.json()
    for item in data.get("response", {}).get("body", {}).get("items", {}).get("item", []):
        print("시도 이름 확인:", item.get("name"))
        if item.get("name") == city:
            area_code = item.get("code")
            sub_url = f"http://apis.data.go.kr/B551011/KorService1/areaCode1?serviceKey={SERVICE_KEY}"
            sub_params = {
                "MobileOS": "ETC",
                "MobileApp": "AppTest",
                "_type": "json",
                "areaCode": area_code,
                "numOfRows": 100
            }
            sub_response = requests.get(sub_url, params=sub_params)
            if sub_response.status_code != 200:
                return None

            sub_data = sub_response.json()
            for sub_item in sub_data.get("response", {}).get("body", {}).get("items", {}).get("item", []):
                if sub_item.get("name") == district:
                    sigungu_code = sub_item.get("code")
                    return area_code, sigungu_code
    return None

# 🔹 (보조 함수) 추천 리스트 가져오기
async def get_api_recommendations(category: str, area_code: str, sigungu_code: str):
    print("[DEBUG] 요청 카테고리:", category)
    print("[DEBUG] 지역 코드:", area_code, sigungu_code)

    CATEGORY_CODE_MAP = {
        "음식점": "39",
        "숙소": "32",
        "관광지": "12",
        "쇼핑": "38"
    }

    content_type_id = CATEGORY_CODE_MAP.get(category)
    if not content_type_id:
        print("[DEBUG] 유효하지 않은 카테고리입니다.")
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

    # 관광지일 때만 cat3 포함 위해 listYN 추가
    if content_type_id == "12":
        params["listYN"] = "Y"

    response = requests.get(url, params=params)
    print("[DEBUG] 상태코드:", response.status_code)

    if response.status_code != 200:
        print("[DEBUG] API 호출 실패")
        return []

    print("[DEBUG] 응답 일부:", response.text[:300])

    try:
        data = response.json()

    # 추가 방어 코드
        if isinstance(data, str):
            import json
            data = json.loads(data)
    except Exception as e:
        print("[DEBUG] JSON 파싱 실패:", e)
        return []


    items = data.get("response", {}).get("body", {}).get("items", {}).get("item", [])
    print("[DEBUG] 추천 결과 개수:", len(items))

    results = []
    for item in items:
        print("[DEBUG] cat3:", item.get("cat3"), "| title:", item.get("title"))
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


