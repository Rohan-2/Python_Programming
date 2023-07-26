import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = "George"
email['to'] = "xyz@gmail.com"
email['subject'] = " You won a million dollors!"

email.set_content("I am a Pyton Master!")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("123@gmail.com", "password")
    smtp.send_message(email)
    print("all good boss!")