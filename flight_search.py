import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()
AMADEUS_API_KEY=os.getenv("AMADEUS_API_KEY")
AMADEUS_API_SECRET=os.getenv("AMADEUS_API_SECRET")
BASE_API_URL = "https://test.api.amadeus.com"

token_url= f"{BASE_API_URL}/v1/security/oauth2/token"
city_search_url = f"{BASE_API_URL}/v1/reference-data/locations/cities"
offer_url = f"{BASE_API_URL}/v2/shopping/flight-offers"

header = {
    "Content-Type": 'application/x-www-form-urlencoded'
}

body = {
    'grant_type': 'client_credentials',
    'client_id':AMADEUS_API_KEY,
    'client_secret': AMADEUS_API_SECRET
}

resp = requests.post(url=token_url, headers=header, data=body)
resp.raise_for_status()
access_token = resp.json()["access_token"]
headers = {
            'Authorization': f'Bearer {access_token}'
        }

class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""
    def __init__(self, city_name):
        self.iata_code = self.get_iata_code(city_name)
    def get_iata_code(self,city_name):

        params = {
            'keyword': city_name.upper(),
            'max': 1
        }
        r = requests.get(url=city_search_url, params=params, headers=headers)
        r.raise_for_status()
        data = r.json()["data"]
        i = ""
        for city in data:
            if 'iataCode' in city:
                i = city['iataCode']

        return i
    def get_offers(self, destination_location_code):
        today = datetime.now()
        tomorrow = (today + timedelta(days=1)).strftime("%Y-%m-%d")
        half_year = (today + timedelta(days=30 * 6)).strftime("%Y-%m-%d")

        query = {
            "originLocationCode": "LON",
            "destinationLocationCode": destination_location_code,
            "departureDate": tomorrow,
            "returnDate": half_year,
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "2",
        }

        resp_data = requests.get(
            url=offer_url,
            headers=headers,
            params=query,
        )
        resp_data.raise_for_status()
        data = resp_data.json()["data"]
        return data
