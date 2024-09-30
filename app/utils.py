import smtplib
import os
from email.mime.text import MIMEText

def send_email(to_address, subject, message):
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = os.getenv("SMTP_PORT")
    smtp_username = os.getenv("SMTP_USERNAME")
    smtp_password = os.getenv("SMTP_PASSWORD")

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = smtp_username
    msg["To"] = to_address

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, [to_address], msg.as_string())
