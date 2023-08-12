import smtplib
import ssl

from dotenv import load_dotenv
import os
load_dotenv()


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "beerankutty1509@gmail.com"
    pasword = os.getenv("PASSWORD")

    context = ssl.create_default_context()
    receiver = "beerankutty1509@gmail.com"
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, pasword)
        server.sendmail(username, receiver, message)


