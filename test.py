from twilio.rest import Client

account_sid = 'AC13ca9197f22f37ed1d02797d60da75d7'
auth_token = 'ea3708375a819e21b1b02ad4d571a219'
client = Client(account_sid, auth_token)

messages = client.messages.list(to = 'whatsapp:+16156565203')

x = []
for record in messages:
    x.append(record.from_)
    
print(set(x))
