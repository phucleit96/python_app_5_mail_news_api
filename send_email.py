import smtplib
import os
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "badboy27796@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "phuc.le.it96@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg=message)

