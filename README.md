# 오픈소스SW기초 5분반 17조

# 국내 여행지 추천 웹 - Korea Trip Mate

## **📝 Project 소개**

국내 여행을 계획하는 사용자들을 위한 지역 기반 맞춤형 여행지 추천 서비스입니다.

관광지, 음식점, 숙소, 쇼핑 장소를 추천하며, 날씨 및 사용자 선호를 고려한 필터링 기능을 제공합니다.

## 👤주요 사용자

- 본 프로젝트는 국내 여행을 계획 중인 내국인과 외국인 이용자 모두를 대상으로 합니다.

## 📌 주요 기능

- 음식점 추천
- 쇼핑 장소 추천
- 숙소 추천
- 날씨 기반 관광지 추천
- 다국어 번역 기능
- 지도 표시 기능 


## 👥 팀원 소개

| 이름 | 전공 | 역할 | GitHub |
|------|------|------|--------|
| 김현정 | 사이버보안학과 | 프론트엔드, 백엔드, GIT 관리, 프로젝트 총괄 | [@anthia-kim](https://github.com/anthia-kim) |
| 정민지 | 통계데이터사이언스학과 | 프론트엔드, 자료조사 | [@minji13](https://github.com/minji13) |
| 최준영 | 소프트웨어학과 | 백엔드 | [@cjy302](https://github.com/cjy302) |


## **📆 Project Timeline**

![image](https://github.com/user-attachments/assets/1181c230-ed4b-43dd-ba6e-6f5fecb16614)



- 5/7 : 1차 발표
- 5/28 : 2차 발표
- 6/11 : (3차) 최종 발표
  
## 🌐 사용 기술 & 오픈 소스

- 개발 언어 : Python
- 백엔드 : FastAPI
- 프론트엔드 : HTML / CSS , Jinja2
- 외부 API
   - TourAPI
  
      한국관광공사에서 제공하는 공공 데이터 API로, 전국 관광지, 숙박, 음식점 등 여행 정보를 조회
    
      사용자 위치나 지역, 카테고리(관광지/음식점/숙소)로 원하는 여행지 데이터를 받아올 때 활용
  
  - OpenWeatherAPI
  
    전 세계 날씨 정보를 실시간으로 제공하는 API
  
    사용자 위치의 현재 날씨(맑음/비/눈/흐림) 표기
  
    날씨 기반 관광지 추천이나 여행 일정 자동 생성 기능에 적용. 날씨에 따라 실내, 실외 여행지 자동 추천 가능
  
  - Kakao Map API
     
     지도 기반 검색 및 위치 시각화 기능 제공

    여행지의 위치를 지도에 표시하거나 사용자 위치 기반 정보 탐색에 활용

- 사용 오픈 소스 
  -  Create-a-Travel-Recommendation-System-using-Content-based-Collaborative-and-Hybrid-Filtering
    
      여행 추천 시스템 오픈소스

      사용자 선호도와 여행지 특성을 반영한 맞춤형 추천 로직 구현에 참고 및 응용
     
  -  translatepy

      여러 언어를 자동 감지하고 다양한 번역 엔진을 활용할 수 있는 Python 라이브러리

      국내 사용자뿐 아니라 **다국어 사용자 지원**을 위한 번역 기능 구현에 사용

      사용자 요청 텍스트를 자동으로 감지하고 원하는 언어로 실시간 번역 제공
     

     
## 📸 프로젝트 결과 (시연 화면)

![image](https://github.com/user-attachments/assets/56fffd18-60cf-4800-ba0f-f8d43559c22b)

아래는 KoreaTripMate 웹 애플리케이션의 실제 실행 화면입니다.  
관광지, 음식점, 숙소 추천 기능과 Kakao Map 기반 위치 시각화를 확인할 수 있습니다.
  
  
