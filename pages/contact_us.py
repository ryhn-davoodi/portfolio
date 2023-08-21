import streamlit as st
from send_email import send_email
st.title("Contact Me")
with st.form("email_form"):
    user_email=st.text_input("your email address")
    message=st.text_area("your message")
    final_message=f"""\
Subject: new message from {user_email}
    
From: {user_email}
{message} 
    """
    sub_btn=st.form_submit_button("submit")
    if sub_btn:
        send_email(final_message)
        st.info("your message sent!")