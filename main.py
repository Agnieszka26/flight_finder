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
        offers = flight_search.get_offers(iata_code)
        for offer in offers:
            flight_data.parse_offer(offer)
            price = float(flight_data.price)
            if price < float(saved_lowest_price):
                notification_manager = NotificationManager(flight_data.get_data())
                notification_manager.send_message()
                data_manager.update_price(row_id, flight_data.get_data()["price"])
                print(f"Jest niższa, update your table and alert. \nprice response: {flight_data.get_data()['price']} \nsaved_lowest_price:{saved_lowest_price}")
            else:
                print(f"nie ma\n{city}"
                      f"\nprice response: {price} \nsaved_lowest_price:{saved_lowest_price}")
    else:
        iata_code = flight_search.iata_code
        print(iata_code)
        data_manager.update_iata_code(row_id, iata_code)
