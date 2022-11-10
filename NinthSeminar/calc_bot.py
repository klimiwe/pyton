import telebot
from calc_rational import *
from calc_complex import calc_c

API_TOKEN = '5761928287:AAEYUkSinJDcrtnlBkUosn_hLQ06oOtZ9ic'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Привет! Я умею считать комплексные и рациональные числа)))\nПосчитаем?")

@bot.message_handler(content_types='text')
def calc_result(message):
    try:
        if 'j' in message.text:
            result = calc_c(message.text)
            bot.send_message(message.chat.id, result)
        else:
            result = so_skobkami(message.text)
            bot.send_message(message.chat.id, result)
    except: bot.send_message(message.chat.id, 'Не могу такое сосчитать(((')


bot.polling()