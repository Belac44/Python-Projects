import requests

SHEETY_URL = "https://api.sheety.co/6ef3c222fa5bc6acd1cbcca65c05f731/flightDeals/prices"

class DataManager:

    def find_cities(self):
        sheety_data = requests.get(url=SHEETY_URL)
        return sheety_data.json()["prices"]

