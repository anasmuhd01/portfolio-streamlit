import streamlit as st
from send_email import send_email
st.header("contact me")

with st.form(key="my_form"):
    user_email = st.text_input("enter your email:")
    raw_message = st.text_area("enter your message:")
    message = f"""\
Subject: New message from {user_email}

From:{user_email}
{raw_message}
"""
    button = st.form_submit_button("submit")

    if button:
        send_email(message)
        st.info("email send successfully ")