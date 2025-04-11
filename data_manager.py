import requests
import os
from dotenv import load_dotenv

load_dotenv()
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
URL_SHEETY_PRICES = os.getenv("URL_SHEETY_PRICES")
URL_SHEETY_USERS = os.getenv("URL_SHEETY_USERS")

sheety_headers = {
    "Authorization": f"Basic {SHEETY_TOKEN}"
}
class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.past_lowest_prices = self.get_lowest_prices()["prices"]

    def get_lowest_prices(self):
        sheety_response = requests.get(url=URL_SHEETY_PRICES , headers=sheety_headers)
        return sheety_response.json()
    def update_iata_code(self, row_id, iata_code):
        body = {
            "price": {
               "iataCode": iata_code
            }
        }
        sheety_update_row = requests.put(url=f"{URL_SHEETY_PRICES}/{row_id}", json=body, headers=sheety_headers)
        sheety_update_row.raise_for_status()
        print(sheety_update_row.text)
    def update_price(self, row_id, price):
        body = {
            "price": {
               "lowestPrice": price
            }
        }
        sheety_update_row = requests.put(url=f"{URL_SHEETY_PRICES }/{row_id}", json=body, headers=sheety_headers)
        sheety_update_row.raise_for_status()
        print(sheety_update_row.text)

    def get_customer_emails(self):
        response = requests.get(url=URL_SHEETY_USERS, headers=sheety_headers)
        response.raise_for_status()
        users = response.json()['users']
        emails = []
        for user in users:
            email = user['whatIsYourEmailAddress ?']
            emails.append(email)
        return emails