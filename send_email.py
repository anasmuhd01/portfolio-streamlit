import smtplib
import ssl

import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "beerankutty1509@gmail.com"
    pasword = "sbbvdfarbygnwcwg"

    context = ssl.create_default_context()
    receiver = "beerankutty1509@gmail.com"
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, pasword)
        server.sendmail(username, receiver, message)
