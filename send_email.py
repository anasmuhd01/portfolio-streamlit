import streamlit as st
import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "beerankutty1509@gmail.com"
    pasword = st.secrets["g_pas"]


    context = ssl.create_default_context()
    receiver = "beerankutty1509@gmail.com"
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, pasword)
        server.sendmail(username, receiver, message)
