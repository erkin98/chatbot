from flask import Blueprint, jsonify,render_template
from twilio.rest import Client
from flask import send_from_directory
import os

customers = Blueprint('customers',__name__)
account_sid = 'AC13ca9197f22f37ed1d02797d60da75d7'
auth_token = 'ea3708375a819e21b1b02ad4d571a219'
client = Client(account_sid, auth_token)

def get_sender():
    senders = []
    
    messages = client.messages.list(to = 'whatsapp:+16156565203')
    for record in messages:
        message = client.messages(record.sid).fetch()
        senders.append(message.from_)
    # senders = [i for i in senders if i not in senders]
    senders = list(set(senders))
    return senders

def get_msg(sender):
    msgs = []
    messages = client.messages.list(from_ = sender,to = 'whatsapp:+16156565203',limit = 10)
    responses = client.messages.list(from_ = 'whatsapp:+16156565203',to = sender,limit = 10)
    for msg,reply in zip(messages,responses):
        message = client.messages(msg.sid).fetch()
        response = client.messages(reply.sid).fetch()
        msgs.append((message.body,response.body))
    return msgs


# @customers.route('/',methods = ['GET','POST'])
# def home():
#     senders = get_sender()
#     if request.method == "POST":
#         sender = request.form['sender'].upper()
#         return redirect(url_for('success', sender=sender))
    
#     return render_template('index.html',senders = senders)
@customers.route('/', defaults={'path': ''})
@customers.route('/<path:path>')
def serve(path):
     
         return render_template('index.html')  


@customers.route('/customers',methods = ['GET','POST'])
def home():
    senders = get_sender()
    # if request.method == "POST":
    #     sender = request.form['sender'].upper()
    #     return redirect(url_for('success', sender=sender))
    return jsonify(data=senders)
    

@customers.route('/<sender>',methods = ['GET','POST'])
def go_sender(sender):
    # return render_template('senders.html',sender = sender,msgs = get_msg(sender))
    return jsonify(data=get_msg(sender))

# @customers.route('/time')
# def get_current_time():
#     return {'time': time.time()}