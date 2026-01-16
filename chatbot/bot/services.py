from typing import Tuple, Optional
from chatbot import db
from chatbot.models import Customer
from chatbot.bot import constants

class BotService:
    def __init__(self):
        self.countries_map = dict((k.lower(), v.lower()) for k, v in constants.COUNTRIES.items())

    def get_or_create_customer(self, sender_num: str) -> Customer:
        customer = Customer.query.filter_by(sender=sender_num).first()
        if not customer:
            customer = Customer(sender=sender_num)
            db.session.add(customer)
            db.session.commit()
        return customer

    def process_message(self, incoming_msg: str, sender_num: str) -> Tuple[str, Optional[str]]:
        """
        Process the incoming message and return the response body and optional media URL.
        """
        self.get_or_create_customer(sender_num)
        
        response_body = ""
        media_url = None
        
        # Check greetings and main flows
        if 'salam' in incoming_msg:
            return constants.MESSAGES['GREETING'], None
            
        if 'xaricdə təhsil' in incoming_msg:
            return constants.MESSAGES['ASK_COUNTRY'], None

        # Check for country matches
        for country, slug in self.countries_map.items():
            if country in incoming_msg:
                return constants.LINKS['COUNTRIES_BASE'] + slug, None

        # Check specific topics
        if 'dil kursu' in incoming_msg:
            return constants.MESSAGES['LANGUAGE_COURSE'].format(constants.LINKS['LANGUAGE_PROGRAM']), None

        for keyword in constants.KEYWORDS_UNI_FEE:
            if keyword in incoming_msg:
                return constants.MESSAGES['UNI_FEE'], None

        if 'ali məktəblər' in incoming_msg:
            return None, constants.LINKS['ALI_MEKTEBLER_IMG']
            
        if 'orta məktəblər' in incoming_msg:
            return None, constants.LINKS['ORTA_MEKTEBLER_IMG']

        for keyword in constants.KEYWORDS_DOCS:
            if keyword in incoming_msg:
                return constants.MESSAGES['DOCS_REQ'], None

        for keyword in constants.KEYWORDS_LANG:
            if keyword in incoming_msg:
                return constants.MESSAGES['LANG_REQ'], None

        for keyword in constants.KEYWORDS_INFO:
            if keyword in incoming_msg:
                return constants.MESSAGES['INFO_REQ'], None

        for keyword in constants.KEYWORDS_ADDRESS:
            if keyword in incoming_msg:
                return constants.MESSAGES['ADDRESS'], None

        for keyword in constants.KEYWORDS_CONTACT:
            if keyword in incoming_msg:
                return constants.MESSAGES['CONTACT'], None

        for keyword in constants.KEYWORDS_RESERVATION:
            if keyword in incoming_msg:
                return constants.MESSAGES['RESERVATION'].format(constants.LINKS['RESERVATION']), None

        # Default fallback
        return constants.MESSAGES['DEFAULT_CONTINUE'], None
