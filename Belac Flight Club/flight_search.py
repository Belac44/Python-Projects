import requests
from datetime import datetime, timedelta
import os

today = datetime.now().strftime("%d/%m/%Y")
date_to = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")

TEQUILA_URL = "https://tequila-api.kiwi.com/v2/search"
TEQUILA_LOCATIONS_SEARCH = "https://tequila-api.kiwi.com"

headers = {"apikey": os.environ["TEQUILA_API_KEY"]}


class FlightSearch:

    def search_city_code(self, city_name):
        params = {"term": city_name, 'location_types': "city"}
        data = requests.get(url=f"{TEQUILA_LOCATIONS_SEARCH}/locations/query", headers=headers, params=params)
        try:
            code = data.json()["locations"][0]["code"]
        except KeyError:
            code = "Not Found"
        finally:
            return code

    def search_cheapest_flight(self, fly_from="LON", fly_to="NYC"):
        data = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": today,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 30,
            "flight_type": "round",
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=TEQUILA_URL, headers=headers, params=data).json()["data"]
        try:
            response[0]
        except IndexError:
            data["max_stopovers"] = 1
            response = requests.get(url=TEQUILA_URL, headers=headers, params=data).json()["data"]
            try:
                response[0]
            except IndexError:
                print(f"No Flight to {fly_to} with less than 2 stops")
            else:
                return response

        else:
            return response
