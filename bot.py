#bot.py

import telebot
import config
import pb
import datetime
import pytz
import json
import traceback


P_TIMEZONE = pytz.timezone(config.TIMEZONE)
TIMEZONE_COMMON_NAME = config.TIMEZONE_COMMON_NAME

bot = telebot.TeleBot(config.TOKEN)
bot.polling(none_stop=True)


@bot.message_handler(commands=['start'])  
def start_command(message):  
    bot.send_message(  
        message.chat.id,  
        'Greetings! I can show you exchange rates.\n' +  
        'To get the exchange rates press /exchange.\n' +  
        'To get help press /help.'  
  )




# import pb
# bot = telebot.TeleBot(config.TOKEN)
# bot.polling(none_stop=True)


# import telebot;
# bot = telebot.TeleBot('974437164:AAGVofDjqO0O4Qi5p1jqa7wNVUMAoQ_524E')

# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
    
#     @bot.message_handler(content_types=['text', 'document', 'audio'])

#         if message.text == "Hi":
#             bot.send_message(message.from_user.id, "Hello, which city are you interested in?")
#         elif message.text == "/help":
#             bot.send_message(message.from_user.id, "This bot for help people and communicate. Choose the city")
#         else:
#             bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
    
# bot.polling(none_stop=True, interval=0)