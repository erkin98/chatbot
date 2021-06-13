# from chatbot.models import Customer,Message, Response
from flask import request,Blueprint
from twilio.twiml.messaging_response import MessagingResponse
# from chatbot import db

bots = Blueprint('bots',__name__)

@bots.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    # sender_num = request.values.get('From', '')
    # send_id = Customer(sender = sender_num)
    # db.drop_all()
    # db.create_all()
    # db.session.add(send_id)
    # i_msg = Message(message = incoming_msg)
    # db.session.add(i_msg)
    # db.session.commit()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    
    if 'salam' in incoming_msg:
        quote = 'Salam.Bizə yazdığınız üçün təşəkkürlər.Sizə necə köməklik edə bilərik?'

        msg.body(quote)
        responded = True

    if ('xaricdə təhsil' or "xaricde tehsil") in incoming_msg:
        quote = 'Xaricdə təhsil üçün büdcəniz nə qədərdir?'

        msg.body(quote)
        responded = True

    if incoming_msg.isdigit():

        if int(incoming_msg) >= 15000:
            quote = "Sizə göndərdiyimiz fayldan xidmətlərimizlə tanış ola bilərsiz"
            msg.body(quote)
            responded = True
        elif int(incoming_msg) < 10000:
            quote = "Sizin məbləğ üçün az sayda universitet var."
            msg.body(quote)
            responded = True
    if not responded:
        quote = "Zəhmət olmasa sualınızı daha anlaşılan formada verin."
        msg.body(quote)

    # our_msg = Response(response = quote)
    # db.session.add(our_msg)
    # o_id = Response(our_id = 'Azeri Student')
    # db.session.add(o_id)
    # db.session.commit()

    return str(resp)

