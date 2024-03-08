import datetime as dt
import smtplib
from random import choice, randint
import pandas

MY_EMAIL = "pythonautomationtester7@gmail.com"
PASSWORD ="tyqh ncfw rein xswe"
NOW = dt.datetime.now()
TODAY = (NOW.month, NOW.day)
PLACEHOLDER = "[NAME]"

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row['month'], row['day']): row for index, row in data.iterrows()}

if TODAY in birthdays_dict:
	random_letter = randint(1, 3)  # Randomly pick a number between 1 and 3
	letter_template_path = f"letter_templates/letter_{random_letter}.txt"

	with open(letter_template_path, "r") as file:
		letter_content = file.read()

	for index, row in data.iterrows():
		if (row['month'], row['day']) == TODAY:
			recipient_name = row['name']
			recipient_email = row['email']
			completed_birthday_letter = letter_content.replace(PLACEHOLDER, recipient_name)

			with open(f"letter_templates/letter_for_{recipient_name}.txt", mode="w") as completed_letter:
				completed_letter.write(completed_birthday_letter)

			with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
				connection.starttls()
				connection.login(user=MY_EMAIL, password=PASSWORD)
				connection.sendmail(
					from_addr=MY_EMAIL,
					to_addrs=recipient_email,
					msg=f"Subject: Happy Birthday!\n\n{completed_birthday_letter}"
				)
				print("Birthday email sent successfully.")

