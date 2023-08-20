import smtplib
import ssl
import os

def send_email(message):
    username="reyhaneh.gh.davodi@gmail.com"
    password=os.getenv("PASSWORD")
    port=465
    host="smtp.gmail.com"
    receiver="reyhaneh.gh.davodi@gmail.com"
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)
