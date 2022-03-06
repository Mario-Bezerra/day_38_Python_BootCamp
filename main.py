import requests
import datetime as dt
from requests.auth import HTTPBasicAuth

today = dt.datetime.now()
day = today.strftime("%d/%m/%Y")
hour = today.strftime("%H:%M")


APP_ID = "xxxxx"
API_KEY = "xxxxxxx"

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
# keys for acess the api
nutri_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
# asking the exercise
exercise = str(input("Tell me what you do today?  "))

# params for the result of the exercise
nutri_params = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 90,
    "height_cm": 185.2,
    "age": 23
}
response_nutri = requests.post(EXERCISE_ENDPOINT, json=nutri_params, headers=nutri_header)
response_nutri.raise_for_status()
data = response_nutri.json()

# setting params for google sheets
params_google_sheets = {
    "workout":{
    "Date" : day,
    "Time" : hour,
    "Exercise" : data['exercises'][0]['name'],
    "Duration" : data['exercises'][0]['duration_min'],
    "Calories" : data['exercises'][0]['nf_calories'],
    }
}
headers = {"Authorization": "Bearer xxxxxx"}
google_sheets_response = requests.post(url="https://api.sheety.co//myWorkouts/workouts",
                                       json=params_google_sheets,
                                       headers=headers)
print(google_sheets_response.text)
