from twilio.rest import TwilioRestClient

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC109189a10859648f3b07841e59b02876"
auth_token = "a6d72e9901e1a72f016a7b2bdedb2396"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Alexandre Ximenes",
    to="+5541996605877",
    from_="+5541991626365")

print(message.sid)
