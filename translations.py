# translations.py

# ✅ 간단한 시/도 이름을 정식 명칭으로 바꿔주는 맵
CITY_NAME_REMAP = {
    "서울": "서울특별시",
    "부산": "부산광역시",
    "대구": "대구광역시",
    "인천": "인천광역시",
    "광주": "광주광역시",
    "대전": "대전광역시",
    "울산": "울산광역시",
    "세종": "세종특별자치시",
    "경기": "경기도",
    "강원": "강원특별자치도",
    "충북": "충청북도",
    "충남": "충청남도",
    "전북": "전북특별자치도",
    "전남": "전라남도",
    "경북": "경상북도",
    "경남": "경상남도",
    "제주": "제주특별자치도",
}

# ✅ 자동 번역 안 되는 시/도 수동 매핑
JAPANESE_CITY_MAP = {
    "서울특별시": "ソウル特別市",
    "부산광역시": "プサン広域市",
    "대구": "大邱広域市",
    "인천": "仁川広域市",
    "광주광역시": "クァンジュ広域市",
    "대전광역시": "テジョン広域市",
    "울산광역시": "ウルサン広域市",
    "세종특별자치시": "セジョン特別自治市",
    "경기도": "キョンギ道",
    "강원특별자치도": "カンウォン特別自治道",
    "충청북도": "チュンチョン北道",
    "충청남도": "チュンチョン南道",
    "전북특별자치도": "チョンブク特別自治道",
    "전라남도": "チョルラ南道",
    "경상북도": "キョンサン北道",
    "경상남도": "キョンサン南道",
    "제주특별자치도": "チェジュ特別自治道"
}

CHINESE_CITY_MAP = {
    "서울특별시": "首尔特别市",
    "부산광역시": "釜山广域市",
    "대구": "大邱广域市",
    "인천": "仁川广域市",
    "광주": "光州广域市",
    "대전광역시": "大田广域市",
    "울산광역시": "蔚山广域市",
    "세종특별자치시": "世宗特别自治市",
    "경기도": "京畿道",
    "강원특별자치도": "江原特别自治道",
    "충청북도": "忠清北道",
    "충청남도": "忠清南道",
    "전북특별자치도": "全北特别自治道",
    "전라남도": "全罗南道",
    "경상북도": "庆尚北道",
    "경상남도": "庆尚南道",
    "제주특별자치도": "济州特别自治道"
}


# ✅ 자동 번역 안 되는 시군구 수동 매핑
JAPANESE_DISTRICT_MAP = {
    "서울특별시": {
        "강남구": "カンナム区",
        "강동구": "カンドン区",
        "강북구": "カンブク区",
        "강서구": "カンソ区",
        "관악구": "クァナク区",
        "광진구": "クァンジン区",
        "구로구": "クロ区",
        "금천구": "クムチョン区",
        "노원구": "ノウォン区",
        "도봉구": "トボン区",
        "동대문구": "トンデムン区",
        "동작구": "トンジャク区",
        "마포구": "マポ区",
        "서대문구": "ソデムン区",
        "서초구": "ソチョ区",
        "성동구": "ソンドン区",
        "성북구": "ソンブク区",
        "송파구": "ソンパ区",
        "양천구": "ヤンチョン区",
        "영등포구": "ヨンドゥンポ区",
        "용산구": "ヨンサン区",
        "은평구": "ウンピョン区",
        "종로구": "チョンノ区",
        "중구": "チュング区",
        "중랑구": "チュンラン区"
    },
    "부산광역시": {
        "강서구": "カンソ区",
        "금정구": "クムジョン区",
        "기장군": "キジャン郡",
        "남구": "ナム区",
        "동구": "トン区",
        "동래구": "トンネ区",
        "부산진구": "プサンジン区",
        "북구": "プク区",
        "사상구": "ササン区",
        "사하구": "サハ区",
        "서구": "ソ区",
        "수영구": "スヨン区",
        "연제구": "ヨンジェ区",
        "영도구": "ヨンド区",
        "중구": "チュング区",
        "해운대구": "ヘウンデ区"
    },
    "대구광역시": {
        "남구": "ナム区",
        "달서구": "タルソ区",
        "달성군": "タルソン郡",
        "동구": "トン区",
        "북구": "プク区",
        "서구": "ソ区",
        "수성구": "スソン区",
        "중구": "チュング区"
    },
    "인천": {
        "강화군": "カンファ郡",
        "계양구": "ケヤン区",
        "미추홀구": "ミチュホル区",
        "남동구": "ナムドン区",
        "동구": "トン区",
        "부평구": "プピョン区",
        "서구": "ソ区",
        "연수구": "ヨンス区",
        "옹진군": "オンジン郡",
        "중구": "チュング区"
    },
    "대전광역시": {
        "동구": "トン区",
        "중구": "チュング区",
        "서구": "ソ区",
        "유성구": "ユソン区",
        "대덕구": "テドク区"
    },
    "광주광역시": {
        "동구": "トン区",
        "서구": "ソ区",
        "남구": "ナム区",
        "북구": "プク区",
        "광산구": "クァンサン区"
    },
    "울산광역시": {
        "중구": "チュング区",
        "남구": "ナム区",
        "동구": "トン区",
        "북구": "プク区",
        "울주군": "ウルジュ郡"
    },
    "세종특별자치시": {
        "세종시": "セジョン市"
    },
    "경기도": {
        "수원시": "スウォン市",
        "성남시": "ソンナム市",
        "고양시": "コヤン市",
        "용인시": "ヨンイン市",
        "부천시": "プチョン市",
        "안산시": "アンサン市",
        "화성시": "ファソン市",
        "남양주시": "ナミャンジュ市",
        "평택시": "ピョンテク市",
        "의정부시": "ウィジョンブ市",
        "시흥시": "シフン市",
        "파주시": "パジュ市",
        "김포시": "キムポ市",
        "광명시": "クァンミョン市",
        "광주시": "クァンジュ市",
        "군포시": "クンポ市",
        "오산시": "オサン市",
        "이천시": "イチョン市",
        "안성시": "アンソン市",
        "구리시": "クリ市",
        "의왕시": "ウィワン市",
        "하남시": "ハナム市",
        "여주시": "ヨジュ市",
        "양평군": "ヤンピョン郡",
        "동두천시": "トンドゥチョン市",
        "과천시": "クァチョン市",
        "가평군": "カピョン郡",
        "연천군": "ヨンチョン郡"
    },
    "강원특별자치도": {
        "춘천시": "チュンチョン市",
        "원주시": "ウォンジュ市",
        "강릉시": "カンヌン市",
        "동해시": "トンヘ市",
        "태백시": "テベク市",
        "속초시": "ソクチョ市",
        "삼척시": "サムチョク市",
        "홍천군": "ホンチョン郡",
        "횡성군": "フェンソン郡",
        "영월군": "ヨンウォル郡",
        "평창군": "ピョンチャン郡",
        "정선군": "チョンソン郡",
        "철원군": "チョルウォン郡",
        "화천군": "ファチョン郡",
        "양구군": "ヤング郡",
        "인제군": "インジェ郡",
        "고성군": "コソン郡",
        "양양군": "ヤンヤン郡"
    },
    "충청북도": {
        "청주시": "清州市",
        "충주시": "忠州市",
        "제천시": "堤川市",
        "보은군": "報恩郡",
        "옥천군": "沃川郡",
        "영동군": "永同郡",
        "진천군": "鎭川郡",
        "괴산군": "槐山郡",
        "음성군": "陰城郡",
        "단양군": "丹陽郡",
        "증평군": "曾坪郡",
        "jeungpyeong-gun": "曾坪郡"
    },
    "충청남도": {
        "천안시": "天安市",
        "공주시": "公州市",
        "보령시": "保寧市",
        "아산시": "牙山市",
        "서산시": "瑞山市",
        "논산시": "論山市",
        "계룡시": "鷄龍市",
        "당진시": "唐津市",
        "금산군": "錦山郡",
        "부여군": "扶餘郡",
        "서천군": "舒川郡",
        "청양군": "青陽郡",
        "홍성군": "洪城郡",
        "예산군": "禮山郡",
        "태안군": "泰安郡"
    },
    "경상북도": {
        "포항시": "浦項市",
        "경주시": "慶州市",
        "김천시": "金泉市",
        "안동시": "安東市",
        "구미시": "龜尾市",
        "영주시": "榮州市",
        "영천시": "榮川市",
        "상주시": "尙州市",
        "문경시": "聞慶市",
        "경산시": "慶山市",
        "군위군": "軍威郡",
        "의성군": "義城郡",
        "청송군": "靑松郡",
        "영양군": "英陽郡",
        "영덕군": "盈德郡",
        "청도군": "淸道郡",
        "고령군": "高靈郡",
        "성주군": "星州郡",
        "칠곡군": "漆谷郡",
        "예천군": "醴泉郡",
        "봉화군": "奉化郡",
        "울진군": "蔚珍郡",
        "울릉군": "鬱陵郡"
    },
    "경상남도": {
        "창원시": "昌原市",
        "진주시": "晋州市",
        "통영시": "統營市",
        "사천시": "泗川市",
        "김해시": "金海市",
        "밀양시": "密陽市",
        "거제시": "巨済市",
        "양산시": "梁山市",
        "의령군": "宜寧郡",
        "함안군": "咸安郡",
        "창녕군": "昌寧郡",
        "고성군": "固城郡",
        "남해군": "南海郡",
        "하동군": "河東郡",
        "산청군": "山淸郡",
        "함양군": "咸陽郡",
        "거창군": "居昌郡",
        "합천군": "陜川郡"
    },
      "전북특별자치도": {
        "전주시": "全州市",
        "군산시": "群山市",
        "익산시": "益山市",
        "정읍시": "井邑市",
        "남원시": "南原市",
        "김제시": "金堤市",
        "완주군": "完州郡",
        "진안군": "鎭安郡",
        "무주군": "茂朱郡",
        "장수군": "長水郡",
        "임실군": "任実郡",
        "순창군": "淳昌郡",
        "고창군": "高敞郡",
        "부안군": "扶安郡"
    },
    "전라남도": {
        "목포시": "木浦市",
        "여수시": "麗水市",
        "순천시": "順天市",
        "나주시": "羅州市",
        "광양시": "光陽市",
        "담양군": "潭陽郡",
        "곡성군": "谷城郡",
        "구례군": "求禮郡",
        "고흥군": "高興郡",
        "보성군": "寶城郡",
        "화순군": "和順郡",
        "장흥군": "長興郡",
        "강진군": "康津郡",
        "해남군": "海南郡",
        "영암군": "靈岩郡",
        "무안군": "務安郡",
        "함평군": "咸平郡",
        "영광군": "靈光郡",
        "장성군": "長城郡",
        "완도군": "莞島郡",
        "진도군": "珍島郡",
        "신안군": "新安郡"
    },
    "제주특별자치도": {
        "제주시": "済州市",
        "서귀포시": "西帰浦市",
        "남제주군": "南済州郡",
        "북제주군": "北済州郡",
        "namjeju-gun": "南済州郡",
        "북부": "北部",
    },
}

CHINESE_DISTRICT_MAP = {
    "서울특별시": {
        "강남구": "江南区",
        "강동구": "江东区",
        "강북구": "江北区",
        "강서구": "江西区",
        "관악구": "冠岳区",
        "광진구": "广津区",
        "구로구": "九老区",
        "금천구": "衿川区",
        "노원구": "芦原区",
        "도봉구": "道峰区",
        "동대문구": "东大门区",
        "동작구": "铜雀区",
        "마포구": "麻浦区",
        "서대문구": "西大门区",
        "서초구": "瑞草区",
        "성동구": "城东区",
        "성북구": "城北区",
        "송파구": "松坡区",
        "양천구": "阳川区",
        "영등포구": "永登浦区",
        "용산구": "龙山区",
        "은평구": "恩平区",
        "종로구": "钟路区",
        "중구": "中区",
        "중랑구": "中浪区"
    },
    "부산광역시": {
        "강서구": "江西区",
        "금정구": "金井区",
        "기장군": "机张郡",
        "남구": "南区",
        "동구": "东区",
        "동래구": "东莱区",
        "부산진구": "釜山镇区",
        "북구": "北区",
        "사상구": "沙上区",
        "사하구": "沙下区",
        "서구": "西区",
        "수영구": "水营区",
        "연제구": "莲堤区",
        "영도구": "影岛区",
        "중구": "中区",
        "해운대구": "海云台区"
    },
    "대구광역시": {
        "남구": "南区",
        "달서구": "达西区",
        "달성군": "达城郡",
        "동구": "东区",
        "북구": "北区",
        "서구": "西区",
        "수성구": "寿城区",
        "중구": "中区"
    },
    "인천": {
        "강화군": "江华郡",
        "계양구": "桂阳区",
        "미추홀구": "弥鄒忽区",
        "남동구": "南洞区",
        "동구": "东区",
        "부평구": "富平区",
        "서구": "西区",
        "연수구": "延寿区",
        "옹진군": "瓮津郡",
        "중구": "中区"
    },
    "대전광역시": {
        "동구": "东区",
        "중구": "中区",
        "서구": "西区",
        "유성구": "儒城区",
        "대덕구": "大德区"
    },
    "광주광역시": {
        "동구": "东区",
        "서구": "西区",
        "남구": "南区",
        "북구": "北区",
        "광산구": "光山区"
    },
    "울산광역시": {
        "중구": "中区",
        "남구": "南区",
        "동구": "东区",
        "북구": "北区",
        "울주군": "蔚州郡"
    },
    "세종특별자치시": {
        "세종시": "世宗市"
    },
    "경기도": {
        "수원시": "水原市",
        "성남시": "城南市",
        "고양시": "高阳市",
        "용인시": "龙仁市",
        "부천시": "富川市",
        "안산시": "安山市",
        "화성시": "华城市",
        "남양주시": "南杨州市",
        "평택시": "平泽市",
        "의정부시": "议政府市",
        "시흥시": "始兴市",
        "파주시": "坡州市",
        "김포시": "金浦市",
        "광명시": "光明市",
        "광주시": "广州市",
        "군포시": "军浦市",
        "오산시": "乌山市",
        "이천시": "利川市",
        "안성시": "安城市",
        "구리시": "九里市",
        "의왕시": "义王市",
        "하남시": "河南市",
        "여주시": "驪州市",
        "양평군": "杨平郡",
        "동두천시": "东豆川市",
        "과천시": "果川市",
        "가평군": "加平郡",
        "연천군": "涟川郡"
    },
    "강원특별자치도": {
        "춘천시": "春川市",
        "원주시": "原州市",
        "강릉시": "江陵市",
        "동해시": "东海市",
        "태백시": "太白市",
        "속초시": "束草市",
        "삼척시": "三陟市",
        "홍천군": "洪川郡",
        "횡성군": "横城郡",
        "영월군": "宁越郡",
        "평창군": "平昌郡",
        "정선군": "旌善郡",
        "철원군": "铁原郡",
        "화천군": "华川郡",
        "양구군": "襄阳郡",
        "인제군": "麟蹄郡",
        "고성군": "高城郡",
        "양양군": "襄阳郡"
    },
     "충청북도": {
        "청주시": "清州市",
        "충주시": "忠州市",
        "제천시": "堤川市",
        "보은군": "报恩郡",
        "옥천군": "沃川郡",
        "영동군": "永同郡",
        "진천군": "镇川郡",
        "괴산군": "槐山郡",
        "음성군": "阴城郡",
        "단양군": "丹阳郡",
        "증평군": "曾坪郡",
        "jeungpyeong-gun": "曾坪郡"
    },
    "충청남도": {
        "천안시": "天安市",
        "공주시": "公州市",
        "보령시": "保宁市",
        "아산시": "牙山市",
        "서산시": "瑞山市",
        "논산시": "论山市",
        "계룡시": "鸡龙市",
        "당진시": "唐津市",
        "금산군": "锦山郡",
        "부여군": "扶余郡",
        "서천군": "舒川郡",
        "청양군": "青阳郡",
        "홍성군": "洪城郡",
        "예산군": "礼山郡",
        "태안군": "泰安郡"
    },
    "경상북도": {
        "포항시": "浦项市",
        "경주시": "庆州市",
        "김천시": "金泉市",
        "안동시": "安东市",
        "구미시": "龟尾市",
        "영주시": "荣州市",
        "영천시": "荣川市",
        "상주시": "尚州市",
        "문경시": "闻庆市",
        "경산시": "庆山市",
        "군위군": "军威郡",
        "의성군": "义城郡",
        "청송군": "青松郡",
        "영양군": "英阳郡",
        "영덕군": "盈德郡",
        "청도군": "清道郡",
        "고령군": "高灵郡",
        "성주군": "星州郡",
        "칠곡군": "漆谷郡",
        "예천군": "醴泉郡",
        "봉화군": "奉化郡",
        "울진군": "蔚珍郡",
        "울릉군": "郁陵郡"
    },
    "경상남도": {
        "창원시": "昌原市",
        "진주시": "晋州市",
        "통영시": "统营市",
        "사천시": "泗川市",
        "김해시": "金海市",
        "밀양시": "密阳市",
        "거제시": "巨济市",
        "양산시": "梁山市",
        "의령군": "宜宁郡",
        "함안군": "咸安郡",
        "창녕군": "昌宁郡",
        "고성군": "固城郡",
        "남해군": "南海郡",
        "하동군": "河东郡",
        "산청군": "山清郡",
        "함양군": "咸阳郡",
        "거창군": "居昌郡",
        "합천군": "陕川郡"
    },
    "전북특별자치도": {
        "전주시": "全州市",
        "군산시": "群山市",
        "익산시": "益山市",
        "정읍시": "井邑市",
        "남원시": "南原市",
        "김제시": "金堤市",
        "완주군": "完州郡",
        "진안군": "镇安郡",
        "무주군": "茂朱郡",
        "장수군": "长水郡",
        "임실군": "任实郡",
        "순창군": "淳昌郡",
        "고창군": "高敞郡",
        "부안군": "扶安郡"
    },
    "전라남도": {
        "목포시": "木浦市",
        "여수시": "丽水市",
        "순천시": "顺天市",
        "나주시": "罗州市",
        "광양시": "光阳市",
        "담양군": "潭阳郡",
        "곡성군": "谷城郡",
        "구례군": "求礼郡",
        "고흥군": "高兴郡",
        "보성군": "宝城郡",
        "화순군": "和顺郡",
        "장흥군": "长兴郡",
        "강진군": "康津郡",
        "해남군": "海南郡",
        "영암군": "灵岩郡",
        "무안군": "务安郡",
        "함평군": "咸平郡",
        "영광군": "灵光郡",
        "장성군": "长城郡",
        "완도군": "莞岛郡",
        "진도군": "珍岛郡",
        "신안군": "新安郡"
    },
    "제주특별자치도": {
        "제주시": "济州市",
        "서귀포시": "西归浦市",
        "남제주군": "南济州郡",
        "북제주군": "北济州郡",
        "namjeju-gun": "南济州郡",
        "북부": "北部",
    },
}

# ✅ 시/도 이름 번역 함수
def translate_city_name(name, lang):
    if lang == "Japanese":
        return JAPANESE_CITY_MAP.get(name)
    elif lang == "Chinese":
        return CHINESE_CITY_MAP.get(name)
    else:
        return None

# ✅ # ✅ 시군구 이름 번역 함수 (city 없이 처리 가능!)
def translate_district_name(district, lang):
    target_map = JAPANESE_DISTRICT_MAP if lang == "Japanese" else (
        CHINESE_DISTRICT_MAP if lang == "Chinese" else None
    )
    if not target_map:
        return None

    # ✅ 모든 시도 딕셔너리를 순회하면서 district를 찾아서 반환
    for city_name, districts in target_map.items():
        if district in districts:
            return districts[district]
    return None
