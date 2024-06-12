import smtplib
from email.message import EmailMessage

message = EmailMessage()
message["Subject"] = "Confirmation code"
message["From"] = "from@example.com"
message["To"] = "to@example.com"
message.set_content("Your confirmation code is 123")

with smtplib.SMTP("localhost", 8025) as s:
    s.send_message(message)
