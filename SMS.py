from twilio.rest import Client

account_sid = 'ACf440bff5ddc424b22a396e678db9d48b'
auth_token = '{your_auth_token}'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12058131203',
    body='Hello Richard! I\'m your Python SMS.',
    to = '+886926802590'
)

print(message.sid)
