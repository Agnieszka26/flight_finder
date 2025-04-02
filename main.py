#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
#to achieve the program requirements.
from pprint import pprint

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

data_manager = DataManager()
sheet_data = data_manager.past_lowest_prices
flights = []

for row in sheet_data:
    city = row["city"]
    flight_search = FlightSearch(city)
    flight_data = FlightData(city)
    if 'iataCode' in row:
        iata_code = row["iataCode"]
        data = flight_search.get_offers(iata_code)
        for flight_offer in data:
            price = flight_offer["price"]['total']
            currency = flight_offer["price"]['currency']
            flight_data.set_price(price)
            itineraries = flight_offer['itineraries']
            for i in itineraries:
                segments = i['segments']
                for s in segments:
                    departure = s['departure']
                    flight_data.set_origin_airport(departure["iataCode"])
                    flight_data.set_out_date(departure["at"])
                    arrival = s['arrival']
                    flight_data.set_return_date(arrival["at"])
                    flight_data.set_destination_airport(arrival["iataCode"])
        flights.append(flight_data)
    else:
        iata_code = flight_search.iata_code
        print(iata_code)
        data_manager.update_lowest_prices(row["id"], iata_code)

