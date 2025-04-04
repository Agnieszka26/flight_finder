# Cheap Flight Finder & Flight Club

## Program Requirements
1. **Cheap Flight Finder:** Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with [International Air Transport Association (IATA)](https://en.wikipedia.org/wiki/IATA_airport_code#Cities_with_multiple_airports) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see [here](https://en.wikipedia.org/wiki/IATA_airport_code#Cities_with_multiple_commercial_airports)).

2. **Cheap Flight Finder:** Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.

3. **Cheap Flight Finder:** If the price is lower than the lowest price listed in the Google Sheet then send an SMS (or WhatsApp Message) to your own number using the Twilio API.

4. **Cheap Flight Finder:** The SMS should include the departure airport IATA code, destination airport IATA code, flight price and flight dates.

5. **Flight Club:** Destinations without Direct Flights: If a direct flight is not found, search Amadeus one more time for that destination to see if there are indirect flights (flights with 1 stop or 2 stops) instead. Capture the cheapest flight price for a flight with a stopover.



## APIs Required

Google Sheet Data Management - https://sheety.co/

Amadeus Flight Search API (Free Signup, Credit Card not required) - https://developers.amadeus.com/

Amadeus Flight Offer Docs - https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api-reference

Amadeus How to work with API keys and tokens guide - https://developers.amadeus.com/get-started/get-started-with-self-service-apis-335

Amadeus Search for Airport Codes by City name - https://developers.amadeus.com/self-service/category/destination-experiences/api-doc/city-search/api-reference

Twilio Messaging (SMS or WhatsApp) API - https://www.twilio.com/docs/messaging/quickstart/python

## environmental variables

Based on file *.env_default* and *APIs Required* create your own privet variables.

## Credits
This project is based on the [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/?) by Angela Yu on Udemy.