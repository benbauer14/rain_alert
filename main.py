import requests
import twilio
from twilio.rest import Client

api_key = ""

weather_params = {
    "lat": "44.876786683641",
    "lon": "-93.4560947576",
    "appid": api_key
}
data = requests.get(f"https://api.openweathermap.org/data/2.5/onecall", params=weather_params)

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)
receiver = "+11234567890"
sender = "+11234567890"

print(message.sid)

gonna_rain = False


def willRain():
    hourly_data = data.json()["hourly"]
    for hours in range(0, 12):

        weather_description = hourly_data[hours]["weather"][0]["description"]
        if "rain" in weather_description:
            global gonna_rain
            gonna_rain = True
            break
    if gonna_rain:
        message = client.messages \
                .create(
                    body="Gonna rain homie!",
                    from_=sender,
                    to=receiver
                )

willRain()