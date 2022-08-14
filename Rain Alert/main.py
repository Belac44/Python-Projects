import requests
API_KEY = "f2f4ce35574887a6886920e3517c1173"
parameters = {
    "lat": -0.281490,
    "lon": 36.078419,
    "exclude": "current,daily,minutely",
    "appid": API_KEY
}
response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()

weather = response.json()
weather_slice = weather["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")

