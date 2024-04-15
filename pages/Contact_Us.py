import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="form"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message here")
    button = st.form_submit_button("Send mail")

    if button:
        send_email(user_email, message)
        st.info("Your email was sent successfully")
