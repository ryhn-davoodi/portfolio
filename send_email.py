import smtplib
import ssl

def send_email(message):
    username="reyhaneh.gh.davodi@gmail.com"
    password="qcoabfzmrqdbsave"
    port=465
    host="smtp.gmail.com"
    receiver="reyhaneh.gh.davodi@gmail.com"
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)
