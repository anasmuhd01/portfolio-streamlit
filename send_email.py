import streamlit as st
import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = st.secrets["mail_id"]
    pasword = st.secrets["g_pas"]


    context = ssl.create_default_context()
    receiver = st.secrets["mail_id"]
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, pasword)
        server.sendmail(username, receiver, message)
