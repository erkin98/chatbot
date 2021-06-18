countries = {"ABŞ":"amerika","Almaniya":"almaniya","Avstraliya":"avstraliya",
        	"Avstriya":"avstriya","Belçika":"belcika",
            	"BƏƏ":"bee","Böyük Britaniya":"boyuk-britaniya",
                "Çexiya":"cexiya","Çin":"cin","Finlandiya":"finlandiya",
                "Fransa":"fransa","Hollandiya":"hollandiya","İrlandiya":"ireland",
                "İspaniya":"spain",	"İsveç":"isvec","İsveçrə":"sweden",	
                "İtaliya":"italy","Kanada":"kanada","Sinqapur":"sinqapur","Türkiyə":"turkiye","Yeni Zelandiya":"yeni-zelandiya"}

countries = dict((k.lower(), v.lower()) for k,v in countries.items())

incoming_msg = 'Salam.konusltasiya üçün vaxt təyin etmək istərdim'.lower()

# if 'f' in incoming_msg:
#     print('x')
#     for i in countries:
#         print(i)
#         if i in incoming_msg:
#             # print(i)
#             print('https://azeristudent.az/countries/' + countries[incoming_msg])
        
if 'konsultasiya' or 'görüş' or 'gorus' or 'gorush' or "rezervasiya" in incoming_msg:

    quote1 = '''Konsultasiya üçün aşağıda qeyd olunan linkə keçid edin 
                --> https://azeristudent.az/reserve/ və ya +994505122828,
                +994502959776, 0124886678 nömrələrinə zəng edin.'''

    print(quote1)