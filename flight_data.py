class FlightData:
    """This class is responsible for store flight data received from Amadeus API"""
    def __init__(self, city):
        self.city = city,
        self.price = "N/A",
        self.origin_airport = "N/A",
        self.destination_airport = "N/A",
        self.out_date = "N/A",
        self.return_date = "N/A",
    def set_price(self, x):
        self.price = x
    def set_origin_airport(self, x):
        self.origin_airport = x
    def set_destination_airport(self, x):
        self.destination_airport = x
    def set_out_date(self, x):
        self.out_date = x
    def set_return_date(self, x):
        self.return_date = x
    def get_data(self):
        return {
            'city': self.city,
            'price': self.price,
            'origin_airport': self.origin_airport,
            'destination_airport': self.destination_airport,
            'out_date': self.out_date,
            'return_date': self.return_date
        }