#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
#to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.past_lowest_prices

for row in sheet_data:
    city = row["city"]
    row_id = row["id"]
    flight_search = FlightSearch(city)
    flight_data = FlightData(city)
    if 'iataCode' in row:
        iata_code = row["iataCode"]
        saved_lowest_price = row["lowestPrice"]
        data = flight_search.get_offers(iata_code)
        for flight_offer in data:
            price = flight_offer["price"]['total']
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
        if float(flight_data.get_data()["price"]) < float(saved_lowest_price):
            notification_manager = NotificationManager(flight_data.get_data())
            notification_manager.send_message()
            data_manager.update_price(row_id, flight_data.get_data()["price"])
            print(f"Jest niższa, update your table and alert. \nprice response: {flight_data.get_data()['price']} \nsaved_lowest_price:{saved_lowest_price}")
        else:
            print(f"nie ma\n{flight_data.get_data()['city'][0]}"
                  f"\nprice response: {flight_data.get_data()['price']} \nsaved_lowest_price:{saved_lowest_price}")
    else:
        iata_code = flight_search.iata_code
        print(iata_code)
        data_manager.update_iata_code(row_id, iata_code)
