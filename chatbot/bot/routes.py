from flask import request, Blueprint
from twilio.twiml.messaging_response import MessagingResponse
from chatbot.bot.services import BotService
import datetime

bots = Blueprint('bots', __name__)
bot_service = BotService()

@bots.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    sender_num = request.values.get('From', '').lower()
    # Log the message SID if needed, or date
    # date = request.values.get('MessageSid') 
    
    response_body, media_url = bot_service.process_message(incoming_msg, sender_num)
    
    resp = MessagingResponse()
    msg = resp.message()
    
    if response_body:
        msg.body(response_body)
    
    if media_url:
        msg.media(media_url)
        
    print(f"Processed message at {datetime.datetime.now()}")
    return str(resp)
