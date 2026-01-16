from flask import Blueprint, jsonify, render_template, request, current_app
from twilio.rest import Client
from chatbot.models import Customer
from typing import List, Tuple

customers = Blueprint('customers', __name__)

def get_twilio_client():
    account_sid = current_app.config['TWILIO_ACCOUNT_SID']
    auth_token = current_app.config['TWILIO_AUTH_TOKEN']
    return Client(account_sid, auth_token)

def get_messages(sender: str) -> List[Tuple[str, str]]:
    client = get_twilio_client()
    whatsapp_number = current_app.config['TWILIO_WHATSAPP_NUMBER']
    
    try:
        limit = request.get_json().get('size', 10)
    except (AttributeError, TypeError):
        limit = 10

    # Fetch messages sent by the user
    messages = client.messages.list(
        from_=sender,
        to=whatsapp_number,
        limit=limit
    )
    
    # Fetch responses sent by the bot
    responses = client.messages.list(
        from_=whatsapp_number,
        to=sender,
        limit=limit
    )
    
    # NOTE: This zip logic assumes a strict 1-to-1 conversation flow which is fragile.
    # Preserving behavior for now as per refactoring guidelines, 
    # but ideally this should fetch all messages and sort by time.
    msgs = []
    for msg, reply in zip(messages, responses):
        # Fetch full body if needed, though list() usually returns body.
        # Original code fetched individual messages again, which is inefficient.
        # Checking if body is available in list object. It is.
        msgs.append((msg.body, reply.body))
        
    return msgs

@customers.route('/', defaults={'path': ''})
@customers.route('/<path:path>')
def serve(path):
    return render_template('index.html')

@customers.route('/customers', methods=['GET'])
def get_all_customers():
    data = Customer.query.all()
    senders = [str(c.sender) for c in data]
    return jsonify(data=senders)

@customers.route('/customers/<sender>', methods=['POST'])
def get_customer_messages(sender):
    # Original code allowed GET but used request.get_json() which fails on GET usually unless body is sent.
    # Changed to POST as per usage in frontend (axios.post)
    return jsonify(data=get_messages(sender))
