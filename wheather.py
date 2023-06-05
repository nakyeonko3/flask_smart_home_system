import requests
from datetime import datetime, timedelta
import pandas as pd

# 변수 설정
api_key = "f792055dde07e71affd9332be092d47d"
city_name = "Samcheok"


# 현재 시간과 내일 날짜 범위 계산
now = datetime.now()
tomorrow = now + timedelta(days=1)
tomorrow_date = tomorrow.strftime("%Y-%m-%d")

# API 요청
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric"
response = requests.get(url)

# 응답 확인
if response.status_code != 200:
    print(f"Error: API request failed with status code {response.status_code}")
    print(response.text)
else:
    data = response.json()

    # 내일 날짜의 데이터만 필터링
    filtered_data = [
        entry for entry in data["list"] if entry["dt_txt"].startswith(tomorrow_date)
    ]

    # 결과 출력
    for entry in filtered_data:
        date_time = entry["dt_txt"]
        temperature = entry["main"]["temp"]
        wind_speed = entry["wind"]["speed"]
        humidity = entry["main"]["humidity"]
        rain = entry["rain"]["3h"] if "rain" in entry and "3h" in entry["rain"] else 0

        print(
            f"Date & Time: {date_time}, Temperature: {temperature}°C, Wind Speed: {wind_speed} m/s, Humidity: {humidity}%, Rain: {rain} mm"
        )

        new_row = {
            "Date & Time": date_time,
            "Temperature(C)": temperature,
            "Wind Speed(m/s)": wind_speed,
            "Humidity(%)": humidity,
            "rain(mm)": rain,
        }

        file_name = "test0518.csv"
        with open(file_name, "a") as f:
            writer = pd.DataFrame([new_row])
            writer.to_csv(f, header=f.tell() == 0, index=False, lineterminator="\n")
