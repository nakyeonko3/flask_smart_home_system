from bs4 import BeautifulSoup
from selenium import webdriver
import re

# import time

URL = "https://www.google.com/search?q=%EC%82%BC%EC%B2%99+%EB%82%A0%EC%94%A8&oq=%EC%82%BC%EC%B2%99+%EB%82%A0%EC%94%A8&aqs=chrome..69i57j0i512j0i30j0i5i30l7.3294j1j7&sourceid=chrome&ie=UTF-8"


# headless 옵션
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

# 드라이버 인스턴스 생성, URL 초기화
driver = webdriver.Chrome(executable_path="chromedriver", options=options)
driver.get(url=URL)

HTML = driver.page_source  # 날씨 구글링한 HTML 페이지 소스코드
soup = BeautifulSoup(HTML, "html.parser")
SVG_TEMP_GRAPH = soup.select("#wob_gsvg > text")  # 날씨 svg 그래프만 따로 추출


def is_temp_text(element):
    """온도가 적힌 html 테그인지 확인하는 함수"""
    return (
        element["style"] == "font:bold 11px arial;text-anchor:middle"
        and element.text != ""
    )


def extract_date(text):
    """날짜만 추출하는 정규식 함수"""
    return re.search(r"\(.*", text).group()


def extract_dayoftheweek(text):
    """요일만 추출하는 정규식 함수"""
    return re.search(r"\((.*?)\)", text).group(1)


def extract_oneweektemperature():
    """일주일 온도와 날짜를 출력함"""
    for element in filter(is_temp_text, SVG_TEMP_GRAPH):
        print(f'날짜: { extract_date(element["aria-label"]) }')
        print(f"요일: { extract_dayoftheweek(element['aria-label']) }")
        print(f"온도: {element.text}")
        # print(element["style"])
    print("break")


extract_oneweektemperature()

driver.quit()
