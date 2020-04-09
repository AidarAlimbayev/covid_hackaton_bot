import telebot
from telebot import types

bot = telebot.TeleBot('974437164:AAHt2f9IRs5Gf2K_3ydD1qB9UteAgndHlFg')

@bot.message_handler(commands=['info'])
def send_message(message):
    bot.send_message(message.from_user.id, 'Общее число диагностированных случаев заражения коронавирусом SARS-CoV-2 по странам на 9 апреля 00:00 ALM \n' +
                                        '🇺🇳Мир: 1,504,665 | жертв: 87,894 | стран и территорий: 225 \n' + 
                                        ':us: США: 425,469 | 14,508 \n' +
                                        ':es: Испания: 146,824 | 14,685 \n' +
                                        ':it: Италия: 139,422 | 17,669 \n' +
                                        ':fr: Франция: 112,950 | 10,689 \n' +
                                        ':de: Германия: 112,113 | 2,208 \n' +
                                        ':cn: Китай: 81,802 | 3,333 \n' +
                                        '🇮🇷Иран: 64,586 | 3,993 \n' +
                                        '🇬🇧Великобритания: 60,773 | 7,097 \n' +
                                        '🇹🇷Турция: 38,226 | 812 \n' +
                                        '🇧🇪Бельгия: 23,403 | 2,240 \n' +
                                        '🇨🇭Швейцария: 23,280 | 895 \n' +
                                        '🇳🇱Нидерланды: 20,549 | 2,248 \n' +
                                        '🇨🇦Канада: 19,195 | 427 \n' +
                                        '🇧🇷Бразилия: 15,927 | 800 \n' +
                                        '🇵🇹Португалия: 13,141 | 380 \n' +
                                        '🇦🇹Австрия: 12,941 | 273 \n' +
                                        ':kr: Южная Корея: 10,384 | 200 \n' +
                                        '🇮🇱Израиль: 9,404 | 73 \n' +
                                        'ru: Россия: 8,672 | 63 \n' +
                                        '🇸🇪Швеция: 8,419 | 687 \n' +
                                        '🇳🇴Норвегия: 6,086 | 101 \n' +
                                        '🇮🇪Ирландия: 6,074 | 235 \n' +
                                        '🇦🇺Австралия: 6,013 | 50 \n' +
                                        '🇮🇳Индия: 5,916 | 178 \n' +
                                        '🇨🇱Чили: 5,543 | 48 \n' +
                                        '🇺🇳Остальные страны: 127,501 | 3,822 \n' +
                                        '... \n' +
                                        '🇺🇦Украина: 1,668 | 52 \n' +
                                        '🇪🇪Эстония: 1,185 | 24 \n' +
                                        '🇲🇩Молдова: 1,174 | 27 \n' +
                                        '🇧🇾Беларусь: 1,066 | 13 \n' +
                                        '🇱🇹Литва: 912 | 15 \n' +
                                        '🇦🇲Армения: 881 | 9 \n' +
                                        '🇦🇿Азербайджан: 822 | 8 \n' +
                                        '🇰🇿Казахстан: 727 | 7 \n' +
                                        '🇱🇻Латвия: 577 | 2 \n' +
                                        '🇺🇿Узбекистан: 545 | 3 \n' +
                                        '🇰🇬Кыргызстан: 270 | 4 \n' +
                                        '🇬🇪Грузия: 211 | 3')

name = ''
email = ''
age = 0
phone = ''
@bot.message_handler(commands=['reg']) 
def get_start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Your name?")
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Your phone number?')
    bot.register_next_step_handler(message, get_phone)

def get_phone(message):
    global phone
    phone = message.text
    bot.send_message(message.from_user.id, 'Your email?')
    bot.register_next_step_handler(message, get_email)


def get_email(message):
    global email
    email = message.text
    bot.send_message(message.from_user.id, 'Your age?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Please enter number')
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Yes', callback_data='yes') #кнопка «Да»
        keyboard.add(key_yes) #добавляем кнопку в клавиатуру
        key_no= types.InlineKeyboardButton(text='No', callback_data='no')
        keyboard.add(key_no)
        question = 'You '+str(age)+' years old, your name is '+name+', contacts '+email+', '+phone+' ?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
        bot.send_message(message.from_user.id, 'For next step press /action')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, 'ok: ')
    elif call.data == "no":
       bot.send_message(call.message.chat.id, 'Decline )')


# @bot.callback_query_handler(func=lambda call: True)  
# def iq_callback(query):  
#     data = query.data  
#     if data.startswith('get-'):  
#         get_start('get-')


@bot.message_handler(commands=['action', 'delivery', 'exchange'])  
def action_command(message):  
    keyboard = telebot.types.InlineKeyboardMarkup()  
    keyboard.row(  
        telebot.types.InlineKeyboardButton('buy', callback_data='delively')  
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
        telebot.types.InlineKeyboardButton('delivery', callback_data='get-deliver')  
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
                                      '1) To get the information press /info. \n' + 
                                      '2) To get help press /help. \n'+
                                      '3) To receive a list of available delivery press /delivery.\n' +
                                      '4) Click on the /exchange you are interested in goods.\n' + 
                                      '5) Click “Update” to receive the current information regarding the request.\n' +
                                      '6) Click /reg to make registration in customers and sellers base. \n' +
                                      '6) The bot supports inline. Type @Covid_help_bot in any chat. \n' + 
                                      'or just say "hi"',
                                      reply_markup=keyboard 
    )  

@bot.message_handler(commands=['pay'])  
def pay_command(message):  
    keyboard = telebot.types.InlineKeyboardMarkup()  
    keyboard.row(  
        telebot.types.InlineKeyboardButton('-100-200 USD', callback_data='delively')  
    )
    keyboard.row(  
        telebot.types.InlineKeyboardButton('-200-500 USD', callback_data='get-sell')  
    )
    keyboard.row(  
        telebot.types.InlineKeyboardButton('-500-1000 USD', callback_data='get-donate')  
    )
    keyboard.row(  
        telebot.types.InlineKeyboardButton('-1000-2000 USD', callback_data='get-chatadvice')  
    )

    bot.send_message(  
        message.chat.id,   
        'Amount range for your service/or how much are you willing to pay:',  
        reply_markup=keyboard  
    )


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup()  
    keyboard.row(  
        telebot.types.InlineKeyboardButton('Nur_Sultan', callback_data='Nur_Sultan')  
    )
    keyboard.row(  
        telebot.types.InlineKeyboardButton('Almaty', callback_data='Almaty')  
    )
    bot.send_message(  
        message.chat.id,   
        'Hello, which city are you interested in? \n',  
        reply_markup=keyboard  
    )

@bot.callback_query_handler(func=lambda c: c.data == 'Nur_Sultan')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')


bot.polling(none_stop=True)