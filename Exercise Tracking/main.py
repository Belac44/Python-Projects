import requests
from datetime import datetime

#nutritionix API
APPLICATION_ID = "ac8d2466"
APPLICATION_KEYS = "f4461bbfa290504de493d3d4893d64c6"

POST_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_POST_URL = "https://api.sheety.co/6ef3c222fa5bc6acd1cbcca65c05f731/workoutTracking/workouts"

headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": APPLICATION_KEYS,
    "Content-Type": "application/json"
}

user_input = input("Tell me which exercise you did: ")

exercise_data = {
    "query": user_input,
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 167.64,
    "age": 21
}
response = requests.post(url=POST_ENDPOINT, json=exercise_data, headers=headers)
data = response.json()
print(data)

today = datetime.now()
for activity in data["exercises"]:
    Date = today.strftime("%Y/%m/%d")
    Time = today.strftime("%H:%M:%S")
    Exercise = activity["name"].title()
    Duration = activity["duration_min"]
    Calories = activity["nf_calories"]

    post_data = {
        "workout": {
            "date": Date,
            "time": Time,
            "exercise": Exercise,
            "duration": Duration,
            "calories": Calories,
            "Content-Type": "application/json"
        }

    }

    response = requests.post(SHEETY_POST_URL, json=post_data, auth=())
    print(response.text)
