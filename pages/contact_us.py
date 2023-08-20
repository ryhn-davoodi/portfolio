import streamlit as st
from send_email import send_email
st.title("Contact Me")
with st.form("email_form"):
    user_email=st.text_input("your email address")
    message=st.text_area("your message")+"\n"+user_email
    sub_btn=st.form_submit_button("submit")
    if sub_btn:
        send_email(message)
        st.write("your message sended!")