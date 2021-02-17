"""Step 1: [Text Messages] Have a collection of preset Messages We Can Send my_messages = [" ", " "]"""

GOOD_MORNING_QUOTES = [
    "Good Morning Love!",
    "I don't cook, I don't clean let me tell you how I got this ring ;"
]


"""Step2: [Send To Our SO] Send Preset Message using API send_message(my_messages[0])"""

from twilio.rest import Client
import schedule
import random


cellphone = 123
twillo_number = 234

def send_message(quote):
    account = ""
    token = ""
    client = Client(account_token)

    client.messages.create(to=cellphone,
                           from_=twillo_number,
                           body=quote)

"""Step3: [Every Morning]  Use Library That can Schedule Text To SO at certain time"""
quote = GOOD_MORNING_QUOTES[random.randint(0, len(GOOD_MORNING_QUOTES))]
schedule.every().day.at("06:30").do(send_message,GOOD_MORNING_QUOTES[0])