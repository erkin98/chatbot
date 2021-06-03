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
    if incoming_msg.isdigit():
    
        if int(incoming_msg) >= 15000:
            quote = "Sizə göndərdiyimiz fayldan xidmətlərimizlə tanış ola bilərsiz"
            msg.body(quote)
            responded = True
        elif int(incoming_msg) < 10000:
            quote = "Sizin məbləğ üçün az sayda universitet var."
            msg.body(quote)
            responded = True
    else:
        if 'salam' in incoming_msg:
            # return a quote
        
            quote = 'Salam,bizə yazdığınız üçün təşəkkürlər.Sizə necə köməklik edə bikərik?'

            msg.body(quote)
            responded = True
        elif 'xaricdə təhsil' or "xaricde tehsil" in incoming_msg:
            # return a cat pic
            # msg.media('https://cataas.com/cat')
            quote = 'Xaricdə təhsil üçün büdcəniz nə qədərdir?'

            msg.body(quote)

            responded = True

    return str(resp)