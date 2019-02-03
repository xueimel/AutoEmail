#!/usr/bin/env python3
import smtplib, ssl
import os
import random
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


sender = #inset sender email
receiver = #insert receiver email

msg = MIMEMultipart("alternative")
msg["Subject"] = #add subject
msg["From"] = sender
msg["To"] = receiver
body = # insert body between quotations
"""\

"""

folder = #insert path for folder destination
pic = folder #adds path to front of pic string
pic += random.choice(os.listdir(folder))
with open(pic, 'rb') as photo:
    image_data = photo.read()

# Turn these into plain/html MIMEText objects
text = MIMEText(body, "plain")
image = MIMEImage(image_data, _subtype=None)

msg.attach(text)
msg.attach(image)

password = #inset password
stmp_server = "smtp.gmail.com" #smtp server; default to gmail; alter as needed
context1 = ssl.create_default_context()
port = 465 #sets ssl port
with smtplib.SMTP_SSL(stmp_server, port, context=context1) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
