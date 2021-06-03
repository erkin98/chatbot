from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello,bot'

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'salam' in incoming_msg:
        # return a quote
       
        quote = 'Salam,bizə yazdığınız üçün təşəkkürlər.Sizə necə köməklik edə bikərik?'

        msg.body(quote)
        responded = True
    if 'xaricdə təhsil' or "xaricde tehsil" in incoming_msg:
        # return a cat pic
        # msg.media('https://cataas.com/cat')
        quote = 'Xaricdə təhsil üçün büdcəniz nə qədərdir?'

        msg.body(quote)

        responded = True
    if incoming_msg > 15000:
        quote = "Sizə göndərdiyimiz fayldan xidmətlərimizlə tanış ola bilərsiz"

    if incoming_msg < 15000:
        quote = "Sizin məbləğ üçün az sayda universitet var."


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',port=port)