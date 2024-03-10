import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 53.381130
MY_LONG = -1.470085
MY_EMAIL = "pythonautomationtester7@gmail.com"
PASSWORD ="tyqh ncfw rein xswe"


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if 49.4 <= iss_latitude <= 58.4 and -5.4 <= iss_longitude <= 4.4:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="battsamih@gmail.com",
                msg=f"Subject: ISS ALERT!\n\nLOOK UP AT THE SKY!"
            )
            print("ISS has been detected.")

    else:
        print("ISS is not here.")




