import os
from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Communication:
    def __init__(self, twilio_account_sid, twilio_auth_token, twilio_phone_number, gmail_username, gmail_password):
        self.twilio_account_sid = twilio_account_sid
        self.twilio_auth_token = twilio_auth_token
        self.twilio_phone_number = twilio_phone_number
        self.gmail_username = gmail_username
        self.gmail_password = gmail_password
        self.client = Client(self.twilio_account_sid, self.twilio_auth_token)

    def send_text_message(self, phone_number, message):
        """
        Sends a text message to the specified phone number using Twilio API
        """
        message = self.client.messages.create(
            body=message,
            from_=self.twilio_phone_number,
            to=phone_number
        )

    def send_email(self, to_email, subject, message):
        """
        Sends an email to the specified email address using Gmail API
        """
        msg = MIMEMultipart()
        msg['From'] = self.gmail_username
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.gmail_username, self.gmail_password)
        text = msg.as_string()
        server.sendmail(self.gmail_username, to_email, text)
        server.quit()

class CRMAIPlugin:
    def __init__(self, communication):
        self.communication = communication

    def send_message(self, phone_number, email, message):
        """
        Sends a text message and email to the specified phone number and email address
        """
        self.communication.send_text_message(phone_number, message)
        self.communication.send_email(email, 'New Message', message)
