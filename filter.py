def filter_places_by_weather(places, weather):
    indoor = {
        "A02030400",  # 공연장, 문화센터, 실내 전시
        "A02010800",  # 사찰, 성당 등 종교시설
    }
    outdoor = {
        "A01010500",  # 공원
        "A02020200",  # 관광특구, 테마공원
        "A02020600",  # 마을, 골목
        "A02020700",  # 체육공원
    }

    if weather in ["Rain", "Snow", "Thunderstorm"]:
        return [p for p in places if p.get("cat3") in indoor]
    else:
        return [p for p in places if p.get("cat3") in outdoor]
