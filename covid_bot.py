import telebot

bot = telebot.TeleBot('974437164:AAHt2f9IRs5Gf2K_3ydD1qB9UteAgndHlFg')


@bot.message_handler(commands=['exchange'])  
def exchange_command(message):  
    keyboard = telebot.types.InlineKeyboardMarkup()  
    keyboard.row(  
        telebot.types.InlineKeyboardButton('USD', callback_data='get-USD')  
    )  
    keyboard.row(  
        telebot.types.InlineKeyboardButton('EUR', callback_data='get-EUR'),  
        telebot.types.InlineKeyboardButton('RUR', callback_data='get-RUR')  
    )  
  
    bot.send_message(  
        message.chat.id,   
        'Click on the currency of choice:',  
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
    bot.send_message(  
        message.chat.id,  
        '1) To receive a list of available delivery press /delivery.\n' +  
        '2) Click on the /exchange you are interested in goods.\n' +  
        '3) Click “Update” to receive the current information regarding the request.\n' +  
        '4) The bot supports inline. Type @Covid_help_bot in any chat and the first letters of a currency.',  
        reply_markup=keyboard  
    )


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'This is telegram bot repository \n' + 
                                      'for help people communicate and \n' +
                                      'exchange goods and products.\n' +
                                      'To get the information press /info .\n' + 
                                      'To get help press /help. \n'+
                                      'or just say "hi"')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'hi':
        bot.send_message(message.chat.id, 'Hello, which city are you interested in? \n' +
                                          '/Nur_Sultan \n' +
                                          '/Almaty')
    elif message.text.lower() == 'buy':
        bot.send_message(message.chat.id, 'Buy, be save!')


bot.polling()