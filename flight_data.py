class FlightData:
    """This class is responsible for store flight data received from Amadeus API"""
    def __init__(self, city):
        self.city = city,
        self.price = "N/A",
        self.origin_airport = "N/A",
        self.destination_airport = "N/A",
        self.out_date = "N/A",
        self.return_date = "N/A",
    def set_price(self, price):
        self.price = price
    def parse_offer(self, offer):
        self.set_price(offer["price"]["total"])
        first_itinerary = offer['itineraries'][0]
        first_segment = first_itinerary['segments'][0]
        last_segment = first_itinerary['segments'][-1]

        self.origin_airport = first_segment['departure']['iataCode']
        self.out_date = first_segment['departure']['at']
        self.destination_airport = last_segment['arrival']['iataCode']
        self.return_date = last_segment['arrival']['at']
    def get_data(self):
        return {
            'city': self.city,
            'price': self.price,
            'origin_airport': self.origin_airport,
            'destination_airport': self.destination_airport,
            'out_date': self.out_date,
            'return_date': self.return_date
        }