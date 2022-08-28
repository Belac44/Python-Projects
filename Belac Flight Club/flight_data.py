class FlightData:
    def __init__(self, airportfrom, airportto, price, local_departure, stop_overs=0, via_city=""):
        self.airportfrom = airportfrom
        self.airportto = airportto
        self.price = price
        self.local_departure = local_departure
        self.stop_overs = stop_overs
        self.via_city = via_city
