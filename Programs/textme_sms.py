from twilio.rest import Client

account_sid = "get from twilio trail user dashboard"
auth_token = "get from twilio trail user dashboard"
client = Client(account_sid, auth_token)

message = client.message.create(
    from_ = "twilio generated number"
    body = "content to be sent"
    to = "number to which sms has to be sent"
)

print(message.sid)
