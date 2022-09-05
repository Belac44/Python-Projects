import requests

SHEETY_URL = "https://api.sheety.co/6ef3c222fa5bc6acd1cbcca65c05f731/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.cities = []

    def find_cities_in_sheet(self):
        response = requests.get(SHEETY_URL)
        self.cities = [city["city"] for city in response.json()["prices"]]
        return self.cities

    def fill_iataCode(self, city, ids):
        data = {
            "price": {
                "iataCode": city
            }
        }
        requests.put(f"https://api.sheety.co/6ef3c222fa5bc6acd1cbcca65c05f731/flightDeals/prices/{ids}", json=data)

    def get_sheet_data(self):
        response = requests.get(SHEETY_URL)
        sheet_data = [city for city in response.json()["prices"]]
        return sheet_data