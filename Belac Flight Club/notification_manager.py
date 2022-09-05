from twilio.rest import Client
import os

class NotificationManager:

    def send_message(self, message):
        client = Client(os.environ["account_sid"], os.environ["auth_token"])

        message = client.messages \
            .create(
                body=message,
                from_=os.environ["from_"],
                to='+254719629908'
            )
        print(message.sid)
