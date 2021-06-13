from twilio.rest import Client
import pandas as pd
from datetime import datetime

account_sid = 'AC13ca9197f22f37ed1d02797d60da75d7'
auth_token = 'ea3708375a819e21b1b02ad4d571a219'
client = Client(account_sid, auth_token)


messages = client.messages.list(to = 'whatsapp:+16156565203',limit = 10)
senders = []
for record in messages:
    message = client.messages(record.sid).fetch()
    senders.append(message.from_)
print(pd.unique(senders))


for i in pd.unique(senders):
    msgs = []
    messages = client.messages.list(from_ = i,to = 'whatsapp:+16156565203',limit=10)
    responses = client.messages.list(from_ = 'whatsapp:+16156565203',to = i,limit=10)

    for msg,reply in zip(messages,responses):
        message = client.messages(msg.sid).fetch()
        response = client.messages(reply.sid).fetch()
        msgs.append((message.body,response.body))
    print((msgs))