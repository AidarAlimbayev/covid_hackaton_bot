import telebot
from telebot import types

bot = telebot.TeleBot('974437164:AAHt2f9IRs5Gf2K_3ydD1qB9UteAgndHlFg')

name = ''
surname = ''
age = 0

@bot.callback_query_handler(func=lambda call: True)  
def iq_callback(query):  
    data = query.data  
    if data.startswith('get-'):  
        get_start('get-')

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, 'Запомню : )')
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Decline )')


@bot.message_handler(content_types=['text'])
def get_start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')

def get_name(message): #получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes') #кнопка «Да»
        keyboard.add(key_yes) #добавляем кнопку в клавиатуру
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_no)
        question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.message_handler(commands=['action'])  
def action_command(message):  
    keyboard = telebot.types.InlineKeyboardMarkup()  
    keyboard.row(  
        telebot.types.InlineKeyboardButton('buy', callback_data='get-buy')  
    )
    keyboard.row(  
        telebot.types.InlineKeyboardButton('sell', callback_data='get-sell')  
    )
    keyboard.row(  
        telebot.types.InlineKeyboardButton('donate/share', callback_data='get-donate')  
    )
    keyboard.row(  
        telebot.types.InlineKeyboardButton('chat, give advice', callback_data='get-chatadvice')  
    )
    keyboard.row(  
        telebot.types.InlineKeyboardButton('non-contact delivery request', callback_data='get-contact')  
    )
    keyboard.row(  
        telebot.types.InlineKeyboardButton('deliver', callback_data='get-deliver')  
    )            

    bot.send_message(  
        message.chat.id,   
        'Are you willing to:',  
        reply_markup=keyboard  
    )

@bot.message_handler(commands=['help'])  
def help_command(message):  
    keyboard = telebot.types.InlineKeyboardMarkup()  
    keyboard.add(  
        telebot.types.InlineKeyboardButton(  
            'Message the operator', url='telegram.me/aidar_alimbayev'  
  )  
    )
    bot.send_message(message.chat.id, 'This is telegram bot repository \n' + 
                                      'for help people communicate and \n' +
                                      'exchange goods and products.\n' +
                                      'To get the information press /info .\n' + 
                                      'To get help press /help. \n'+
                                      '1) To receive a list of available delivery press /delivery.\n' +
                                      '2) Click on the /exchange you are interested in goods.\n' + 
                                      '3) Click “Update” to receive the current information regarding the request.\n' +
                                      '4) The bot supports inline. Type @Covid_help_bot in any chat and the first letters of a currency.\n' + 
                                      'or just say "hi"',
                                      reply_markup=keyboard 
    )  



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello, which city are you interested in? \n' +
                                      '/Nur_Sultan \n' +
                                      '/Almaty')



@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'hi':
        bot.send_message(message.chat.id, 'Hello, which city are you interested in? \n' +
                                      '/Nur_Sultan \n' +
                                      '/Almaty')
    elif message.text.lower() == 'buy':
        bot.send_message(message.chat.id, 'Buy, be save!')


bot.polling(none_stop=True)