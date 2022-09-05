from datetime import datetime
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

fly_from = "LON"

cities = DataManager()
search = FlightSearch()
send_not = NotificationManager()


#fill sheet with IATA Codes

for (city, id) in zip(cities.find_cities_in_sheet(), range(2, len(cities.find_cities_in_sheet()) + 2)):
    city_code = search.search_city_code(city)
    print(f"Added {city_code}")
    cities.fill_iataCode(city_code, id)


#Find lowest Price and Send notification
for codes in cities.get_sheet_data():
    data = search.search_cheapest_flight(fly_from=fly_from, fly_to=codes["iataCode"])
    try:
        available = data[0]
    except TypeError:
        continue
    else:
        for item in data:
            date = datetime(int(item["local_departure"].split("-")[0]), int(item["local_departure"].split("-")[1]),
                            int(item["local_departure"].split("-")[2].split("T")[0]))
            airport_data = FlightData(
                airportfrom=f'{item["cityFrom"]}-{item["route"][0]["flyFrom"]}',
                airportto=f'{item["cityTo"]}-{item["route"][-1]["flyFrom"]}',
                price=item["price"],
                local_departure=f'{date.strftime("%d-%m-%Y")}'
            )
            if airport_data.price < codes["lowestPrice"]:
                message = (f"Low price alert!! Only ${airport_data.price} from {airport_data.airportfrom} to "
                           f"{airport_data.airportto} from {airport_data.local_departure}")
                # send_not.send_message(message)
                print(message)
