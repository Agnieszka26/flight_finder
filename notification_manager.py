
from twilio.rest import Client
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")
GMAIL_HOST_NAME = os.getenv("GMAIL_HOST_NAME")
PORT = int(os.getenv("PORT"))
TIMEOUT= int(os.getenv("TIMEOUT"))

class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""
    def __init__(self,data):
        self.text = (f"Low price alert for {data['city'][0]}! Only GBP{data['price']} to fly from {data['origin_airport']} to {data['destination_airport']}, "
                     f"on {data['out_date']} until {data['return_date']}")

    def send_message(self):
        client = Client(account_sid, auth_token)
        message = client.messages.create(from_='+15595127946', to='+48724356310', body=self.text)
        print(message.status)

    def send_email(self, to_addrs):
        with smtplib.SMTP(GMAIL_HOST_NAME, PORT, timeout=TIMEOUT) as connection:
            connection.starttls()
            connection.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
            connection.sendmail(from_addr=GMAIL_ADDRESS, to_addrs=to_addrs, msg=f"Subject: Low Price Alert!\n\n{self.text}")

