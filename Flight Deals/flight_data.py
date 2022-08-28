import requests
from datetime import datetime, timedelta

TEQUILA_URL = "https://tequila-api.kiwi.com/v2/search"
TEQUILA_API_KEY = "zAGXObzArom8aFztMcZKLfoiEo1k6xH_"


today = datetime.now()

headers = {
    "apikey": TEQUILA_API_KEY
}


class FlightData:
    def make_request(self, city_name):
        TEQUILA_PARAMETERS = {
            "fly_from": "LON",
            "fly_to": city_name,
            "dateFrom": today.strftime("%d/%m/%Y"),
            "dateTo": (datetime.now() + timedelta(180)).strftime("%d/%m/%Y")
        }
        response = requests.get(url=TEQUILA_URL, params=TEQUILA_PARAMETERS, headers=headers)
        response.raise_for_status()
        return response.json()["data"]
