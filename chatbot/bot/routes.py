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
    
    countries = {"ABŞ":"amerika","Almaniya":"almaniya","Avstraliya":"avstraliya","ABS":"amerika",
        	"Avstriya":"avstriya","Belçika":"belcika","Belcika":"belcika",
            	"BƏƏ":"bee","Böyük Britaniya":"boyuk-britaniya","İngiltərə":"boyuk-britaniya",
                "Çexiya":"cexiya","Çin":"cin","Finlandiya":"finlandiya","chexiya":"cexiya","chin":"cin","cin":"cin","cexiya":"cexiya",
                "Fransa":"fransa","Hollandiya":"hollandiya",'niderland':"hollandiya","İrlandiya":"ireland",
                "İspaniya":"spain",	"İsveç":"isvec","İsveçrə":"sweden",	"isvec":"Isvec","Isvecre":"sweden",
                "İtaliya":"italy","Kanada":"kanada","Sinqapur":"sinqapur","Türkiyə":"turkiye","Yeni Zelandiya":"yeni-zelandiya","Turkiye":"turkiye"}

    uni_fee = ['tehsil haqqi','təhsil haqqı','tehsil xerci','təhsil xərci','odenis','ödəniş','odenish','qiymet','qiymət']
    docs = ['sened' , 'sened qebulu' , 'sənəd' , 'sənəd qəbulu']
    lang = ['dil bilikleri' , 'dil bilikləri' , 'IELTS' , 'TOEFL']
    info = ['etrafli melumat' , 'ətraflı məlumat' , 'detalli melumat' , 'detallı məlumat' , 'detal']
    adres = ['adress' , 'adres' , 'unvan' , 'ünvan' , 'harda' , 'harada']
    con = ['elaqe' , 'əlaqə' , 'telfon' , 'telefon' , 'nömrə' , 'nomre']
    res = ['konsultasiya' , 'görüş' , 'gorus' , 'gorush' , "rezervasiya"]

    countries = dict((k.lower(), v.lower()) for k,v in countries.items())

    if 'salam' in incoming_msg :
        quote = '\'Salam.Siz Azeri Studentin chatbotu ilə əlaqədəsiniz.Sizə necə kömək edə bilərik?\''

        msg.body(quote)
        responded = True

    elif 'xaricdə təhsil' in incoming_msg :
        quote1 = 'Hansı ölkənin təhsil müəssisələri ilə maraqlanırsınız?'
    
        msg.body(quote1)
      
    elif incoming_msg in countries:
                msg.body('https://azeristudent.az/countries/' + countries[incoming_msg])
                responded = True

    else:
        if 'dil kursu' in incoming_msg:
            quote1 = 'Aktiv dil kursları ilə bağlı məlumat almaq üçün saytımıza daxil olun'
            quote2 = '--> https://azeristudent.az/language-program/'

            msg.body(quote1)
            msg.body(quote2)
            responded = True
            

        else:
            if incoming_msg in uni_fee:

                quote1 = 'Ödənişlər standart deyil, ətraflı məlumat üçün sizə uyğun düyməni sıxın.Qeyd edək ki,universitetlər 2 hissəli şəkildə ödənişə icazə verir.'

                msg.body(quote1)
                responded = True

                if 'ali məktəblər' in incoming_msg:
                    msg.media('https://i.imgur.com/PfeCzCm.jpeg')
                
                elif 'orta məktəblər' in incoming_msg:
                    msg.media('https://i.imgur.com/j0XE3ro.jpeg')


            elif  incoming_msg in docs:

                quote1 = 'Tələb olunan sənədlər:3 tövsiyyə məktubu; Akademik esse; Motivasiya məktubu; CV/Resume; Transkriptlər.'

                msg.body(quote1)
                responded = True

            elif  incoming_msg in lang:

                quote1 = 'Əsasən IELTS və TOEFL dərəcələri tələb olunur.'

                msg.body(quote1)
                responded = True

            elif  incoming_msg in info:

                quote1 = '''Daha ətraflı məlumatları konsultanlarımızdan əldə edə bilərsiniz.Əgər sizə uyğundursa nömrənizi, ad və soyadınızı qeyd edin, müvafiq əməkdaşımız zəng edib konsultasiya üçün vaxt təyin etsin.'''

                msg.body(quote1)
                responded = True


            elif  incoming_msg in adres:

                quote1 = '''Ofisimiz Bakı şəhəri, 8 Noyabr(Nobel) pr.15, Azure Biznes Mərkəzi 20-ci mərtəbə, ofis - 135 ünvanında yerləşir.'''

                msg.body(quote1)
                responded = True

            elif  incoming_msg in con:

                quote1 = '''+994505122828
+994502959776
+994124886678'''

                msg.body(quote1)
                responded = True

            elif  incoming_msg in res:

                quote1 = '''Konsultasiya üçün aşağıda qeyd olunan linkə keçid edin 
                            --> https://azeristudent.az/reserve/ və ya +994505122828,
                            +994502959776, 0124886678 nömrələrinə zəng edin.'''

                msg.body(quote1)
                responded = True

            else:
                quote1 = 'Davam edə bilmək üçün, zəhmət olmasa, yuxarıdakı düymələrdən birini seçin.'

                msg.body(quote1)
                responded = True
    # if ('xaricdə təhsil' or "xaricde tehsil") in incoming_msg:
    #     quote = 'Xaricdə təhsil üçün büdcəniz nə qədərdir?'

    #     msg.body(quote)
    #     responded = True

    #     if incoming_msg.isdigit():

    #         if int(incoming_msg) >= 15000:
    #             quote = "Sizə göndərdiyimiz fayldan xidmətlərimizlə tanış ola bilərsiz"
    #             msg.body(quote)
    #             responded = True
    #         elif int(incoming_msg) < 10000:
    #             quote = "Sizin məbləğ üçün az sayda universitet var."
    #             msg.body(quote)
    #             responded = True
    #     if not responded:
    #         quote = "Zəhmət olmasa sualınızı daha anlaşılan formada verin."
    #         msg.body(quote)

    # our_msg = Response(response = quote)
    # db.session.add(our_msg)
    # o_id = Response(our_id = 'Azeri Student')
    # db.session.add(o_id)
    # db.session.commit()

    return str(resp)

