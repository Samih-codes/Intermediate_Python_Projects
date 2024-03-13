import requests
from twilio.rest import Client

MY_LAT = 53.381130
MY_LONG = -1.470085
api_key = "YOUR_KEY"
account_sid = "YOUR_TWILIO_ID"
auth_token = "YOUR_TOKEN"

parameters = {
	"lat": MY_LAT,
	"lon": MY_LONG,
	"appid": api_key,
	"cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
#print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
	condition_code = hour_data["weather"][0]["id"]
	if int(condition_code) < 700:
		will_rain = True

if will_rain:
	client = Client(account_sid,auth_token)
	message = client.messages.create(
		from_='whatsapp:twilio_number',
		body='It is going to rain today. Bring your Umbrella ☂️',
		to='whatsapp:my_number')
print(message.status)


