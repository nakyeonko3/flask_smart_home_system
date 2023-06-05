import requests

api_key = "f792055dde07e71affd9332be092d47d"
city_name = "Samcheok"
lat = 37.4498745
lon = 129.1652969


def get_wheather():
    url = f"http://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=hourly,daily&appid={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: API request failed with status code {response.status_code}")
        print(response.text)
    else:
        print(response.json())


def get_geometry():
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={5}&appid={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: API request failed with status code {response.status_code}")
        print(response.text)
    else:
        print(response.json())


get_geometry()
get_wheather()
