import telebot
import config
from telebot import types
import http.client

bot=telebot.TeleBot(config.TOKEN)

conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "72ccabb70amsh27b43378ab274c0p119443jsnc7cb3f194139",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"}
conn.request("GET", "/api/npm-covid-data/asia", headers=headers)
res = conn.getresponse()
data = res.read()
js=(data.decode("utf-8"))

countries=['Japan','China','Maldives','Sri Lanka','Singapore']
def datap(country):

    t1=country
    t2="Total Cases:"
    t3="New Cases:"
    t4="Total Deaths:"
    t5="New Deaths:"
    t6="Population:"
        
        
    d1 = js.find('TotalCases',js.find(country))
    d11 = js.find('NewCases',js.find(country))
    tc=js[d1+12:d11-2]
            
    d2 = js.find('NewCases',js.find(country))
    d22 = js.find('TotalDeaths',js.find(country))
    nc=js[d2+10:d22-2]

    d3 = js.find('TotalDeaths',js.find(country))
    d33 = js.find('NewDeaths',js.find(country))
    td=js[d3+13:d33-2]
            
    d4 = js.find('NewDeaths',js.find(country))
    d44 = js.find('TotalRecovered',js.find(country))
    nd=js[d4+11:d44-2]

    d5 = js.find('Population',js.find(country))
    d55 = js.find('one_Caseevery_X_ppl',js.find(country))
    p=js[d5+13:d55-3]

    res=t1 + '\n' + t2 + tc + '\n'+ t3 + nc + '\n' + t4 + td + '\n' + t5 + nd + '\n'+ t6 + p + '\n'
        
    return res

def search(message):
    req=message.text
    if req not in js:
        bot.send_message(message.chat.id,'немає інформації про таку країну :(')
    else:
        bot.send_message(message.chat.id,datap(req))
        

@bot.message_handler(commands=['start'])
def welcome(message):

    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton('вивести статистику по 5-ти країнам')
    item2=types.KeyboardButton('пошук за назвою країни')
    markup.add(item1,item2)
    bot.send_message(message.chat.id,"ласкаво просимо! :)\nцей бот виводить інформацію про захворюваність на ковід у різних країнах континенту азії\nвиберіть опцію".format(message.from_user,bot.get_me()),
    parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def butns(message):
    if message.text=='вивести статистику по 5-ти країнам':
        for i in range(len(countries)):
            textr=datap(countries[i])
            bot.send_message(message.chat.id,textr)
        markup=types.InlineKeyboardMarkup(row_width=1)
        item3=types.InlineKeyboardButton('завантажити файл',callback_data='file')
        markup.add(item3)
        bot.send_message(message.chat.id, 'бажаєте завантажити .txt фійл з результатами?', reply_markup=markup)
    elif message.text=='пошук за назвою країни':
            bot.send_message(message.chat.id,'введіть назву країни (з великої букви, англійською мовою, лише країни континента азії)')
            bot.register_next_step_handler(message,search)
    else:
        bot.send_message(message.chat.id,'не знаю, що відповісти :о')



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'file':
                f=open('covidbot.txt','w')
                f.close()
                f1=open('covidbot.txt','a')
                for i in range(len(countries)):
                    textrr=datap(countries[i])
                    f1.write(textrr)
                f1.close()
                f2=open('covidbot.txt','rb')
                bot.send_document(call.message.chat.id,f2)
                f2.close()
                bot.send_message(message.chat.id,'виберіть опцію для продовження роботи :)')

            
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='завантажити .txt фійл з результатами',reply_markup=None)
    except Exception as e:
        print(repr(e))
 

bot.polling(none_stop=True)
