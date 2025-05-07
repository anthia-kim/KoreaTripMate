def filter_places_by_weather(places, weather):
    indoor = {"A02010100", "A02010200", "A02010500", "A02010900"}  # 실내
    outdoor = {"A01010100", "A01010300", "A01010600", "A02020200"}  # 실외

    if weather in ["Rain", "Snow", "Thunderstorm"]:
        return [p for p in places if p.get("cat3") in indoor]
    else:
        return [p for p in places if p.get("cat3") in outdoor]
