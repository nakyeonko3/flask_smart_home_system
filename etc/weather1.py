import requests
import time

API_KEY = "bf91f0d9592cd579411d4f97f1550d09"
LOCATION = "Seoul,kr"  # 변경하려면 이곳에 도시와 국가 코드 입력
UNITS = "metric"  # 섭씨온도를 원한다면 'metric', 화씨온도를 원한다면 'imperial' 입력

def get_weather_data():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={LOCATION}&appid={API_KEY}&units={UNITS}"
    response = requests.get(url)
    data = response.json()

    weather_desc = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]

    return weather_desc, temperature, feels_like

while True:
    weather_desc, temperature, feels_like = get_weather_data()
    print(f"오늘 날씨: {weather_desc}, 온도: {temperature}°C, 체감온도: {feels_like}°C")

    time.sleep(1)  # 1초 간격으로 날씨 정보 출력
