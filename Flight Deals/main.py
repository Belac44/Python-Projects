from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch

sheet_data = DataManager()
flight_data = FlightData()
flight_search = FlightSearch()

for items in sheet_data.find_cities():
    flight_data_returned = flight_data.make_request(items["iataCode"])
    for dest in flight_data_returned:
        if flight_search.lower_price_notifier(items["lowestPrice"], dest["price"]):
            print(items["city"], "->", dest["price"])


