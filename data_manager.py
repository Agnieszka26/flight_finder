import requests
import os
from dotenv import load_dotenv

load_dotenv()
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
URL_SHEETY = "https://api.sheety.co/cc0f67e3ac3f79b768d391db8f872fd0/flightDeals/prices"

sheety_headers = {
    "Authorization": f"Basic {SHEETY_TOKEN}"
}
class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.past_lowest_prices = self.get_lowest_prices()["prices"]

    def get_lowest_prices(self):
        sheety_response = requests.get(url=URL_SHEETY, headers=sheety_headers)
        return sheety_response.json()
    def update_iata_code(self, id, iata_code):
        body = {
            "price": {
               "iataCode": iata_code
            }
        }
        sheety_update_row = requests.put(url=f"{URL_SHEETY}/{id}", json=body, headers=sheety_headers)
        sheety_update_row.raise_for_status()
        print(sheety_update_row.text)
    def update_price(self, id, price):
        body = {
            "price": {
               "lowestPrice": price
            }
        }
        sheety_update_row = requests.put(url=f"{URL_SHEETY}/{id}", json=body, headers=sheety_headers)
        sheety_update_row.raise_for_status()
        print(sheety_update_row.text)