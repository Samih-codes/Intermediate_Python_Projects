import requests
from datetime import datetime
import os

# Set environment variables before running the script
GENDER = os.environ.get("GENDER")
WEIGHT_KG = os.environ.get("WEIGHT_KG")
HEIGHT_CM = os.environ.get("HEIGHT_CM")
AGE = os.environ.get("AGE")

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

natural_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/0681546c6478651c45ece0c412069b26/pythonWorkoutTracker/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

# Get exercise input from user
exercise_input = input("Tell me what exercises you did? ")

user_params = {
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "query": exercise_input
}

response = requests.post(url=natural_exercise_endpoint, json=user_params, headers=headers)

# Check if request was successful
if response.status_code == 200:
    result = response.json()
    print(result)

    today_date = datetime.now().strftime("%d/%m/%Y")
    now_time = datetime.now().strftime("%X")

    for exercise in result["exercises"]:
        g_sheet_inputs = {
            "workout": {
                "date": today_date,
                "time": now_time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }

        sheet_response = requests.post(sheety_endpoint, json=g_sheet_inputs)

        # Check if sheet request was successful
        if sheet_response.status_code == 200:
            print(sheet_response.text)
        else:
            print("Failed to add workout to sheet.")
else:
    print("Failed to fetch exercises.")
