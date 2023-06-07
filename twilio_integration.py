import twilio
from twilio.rest import Client

def send_sms(device_number, message):
    # Your Account SID and Auth Token from twilio.com/console
    account_sid = 'YOUR_ACCOUNT_SID'
    auth_token = 'YOUR_AUTH_TOKEN'
    client = Client(account_sid, auth_token)
    
    # Send the SMS message using Twilio API
    message = client.messages \
                    .create(
                         body=message,
                         from_='+1TWILIO_NUMBER',
                         to=device_number
                     )

    print('SMS sent to ' + device_number + ' with Message Id: ' + message.sid)
