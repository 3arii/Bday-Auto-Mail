import os
import smtplib
from email.message import EmailMessage
from datetime import date

EMAIL_ADDRESS = "your e-mail address here"
EMAIL_PASSWORD = input("Please enter your password:")

# For security measures I would reccomend using environment variables
# While declaring sensitive info like your e-mail and password
# I have some helpful documentation for windows in the README file
# if you use Linux I assume you already now how to make environs:)


class Friend:

    def __init__(self, name, bday, email):
        self.name = name
        self.bday = bday
        self.email = email

#-------------------DEFINE FRIENDS HERE-------------------#


f1 = Friend("Friend name", "Birt day date", "Email")

#---------------------------------------------------------#

today = str(date.today())

if today == f1.bday:

    msg = EmailMessage()
    msg["Subject"] = f"Happy birthday {f1.name}!"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = f1.email
    msg.set_content(f"Happy birthday {f1.name}!")

    # SMTP cryption for security measures
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        smtp.send_message(msg)
