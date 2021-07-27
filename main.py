import requests

api_key = "d562fb9cb9c7ae37f25eb6c3c61b83c2"

weather_params = {
    "lat": "44.876786683641164",
    "lon": "-93.4560947576714",
    "appid": api_key
}
data = requests.get(f"https://api.openweathermap.org/data/2.5/onecall", params=weather_params)



print(data.status_code)
print(data.json())
print(data.json()["hourly"][0]["weather"])
