import telebot
from telebot import types
#Получение Токена бота
TOKEN = "no)"
bot = telebot.TeleBot(TOKEN)

#Приветствие
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton("МЕНЮ", callback_data='menu')

    markup.add(item)

    bot.send_photo(message.chat.id, open('3hunna.jpg', 'rb'))
    bot.send_message(message.chat.id, "Приветствуем тебя на боте <b>3Hunna Store</b>, {1.first_name}! \n"
                                      "\n"
                                      "Здесь ты сможешь увидеть весь ассортимент который есть в <b>3Hunna Store</b> \n"
                                      "\n"                             
                                      "<b>Чтобы открыть меню нажми на кнопку ниже! </b>"
                     , parse_mode= 'html',                                                   #Парс HTML
                     reply_markup=markup)                                                    #Привязка кнопки к сообщению



@bot.callback_query_handler(func=lambda call: True)
def menu(call):
    try:
        if call.message:
            if call.data == "menu":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Мужская 👨" )                                   #Кнопки клавиатуры
                item2 = types.KeyboardButton("Женская 👩" )
                item3 = types.KeyboardButton("Связь с нами 💌")

                markup.add(item1, item2, item3)                                                    #Добавление кнопок клавиатуры

                bot.send_message(call.message.chat.id, "<b>Что же ты хочешь посмотреть?</b>"
                                 , parse_mode='html'
                                 , reply_markup = markup)

    except Exception as e:
        print(repr(e))
################## КНОПКИ СВЯЗИ #############################
@bot.message_handler(commands= ['url'] )
def url(message):

    markup = types.InlineKeyboardMarkup()
    pokupka = types.InlineKeyboardButton(text='Покупка 🛍', url='https://t.me/be_nice2me')
    razrab = types.InlineKeyboardButton(text='Работа бота ⚙', url='https://t.me/bigi_do_smoke')

    markup.add(pokupka, razrab)

    bot.send_message(message.chat.id, "К кому обратиться?", reply_markup=markup)
#############################################################

######################## ТЕКСТОВОЙ ОБРАБОТЧИК ################
@bot.message_handler(content_types=['text'])
def gender(message):
    if message.chat.type == 'private':
        if message.text == 'Мужская 👨':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Футболки 👕")
            item2 = types.KeyboardButton("Свитеры 🧶")
            item4 = types.KeyboardButton("Обувь 👟")
            item3 = types.KeyboardButton("Вернуться в начало!")

            markup.add(item1, item2, item4, item3)

            bot.send_message(message.chat.id, "Выбери тип одежды"
                             , reply_markup= markup)

        elif message.text == 'Женская 👩':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Кроп-топы 👚")
            item2 = types.KeyboardButton("Сумки 👜")
            item4 = types.KeyboardButton("Аксессуары 💍")
            item5 = types.KeyboardButton("Платья 👗")
            item6 = types.KeyboardButton("Куртки 🧥")
            item7 = types.KeyboardButton("Штаны 👖")
            item3 = types.KeyboardButton("Вернуться в начало!")

            markup.add(item1, item5, item6, item7, item2, item4, item3)

            bot.send_message(message.chat.id, "Выбери тип одежды"
                             , reply_markup= markup)
######################### Обратно в меню ###################################
        elif message.text == 'Вернуться в начало!':
            bot.send_message(message.chat.id, "Вы вернулись в начало!", reply_markup=types.ReplyKeyboardRemove())
            send_welcome(message)

######################### Обращение к функции связи #########################
        elif message.text == 'Связь с нами 💌':
            url(message)
################################  МУЖСКОЕ ###################################
        elif message.text == 'Футболки 👕':
            bot.send_message(message.chat.id, "https://t.me/store3hunna/4")
            bot.send_message(message.chat.id, "https://t.me/store3hunna/6")
            bot.send_message(message.chat.id, "https://t.me/store3hunna/8")
            bot.send_message(message.chat.id, "https://t.me/store3hunna/10")

        elif message.text == 'Свитеры 🧶':
            bot.send_message(message.chat.id, "https://t.me/store3hunna/12")
            bot.send_message(message.chat.id, "https://t.me/store3hunna/14")

        elif message.text == 'Обувь 👟':
            bot.send_message(message.chat.id, "https://t.me/store3hunna/53")
###################### ЖЕНСКОЕ #######################################

        elif message.text == 'Кроп-топы 👚':
            bot.send_message(message.chat.id, "https://t.me/store3hunna/30")
            bot.send_message(message.chat.id, "https://t.me/store3hunna/35")
            bot.send_message(message.chat.id, "https://t.me/store3hunna/39")

        elif message.text == 'Сумки 👜':
            bot.send_message(message.chat.id, "https://t.me/store3hunna/43")
            bot.send_message(message.chat.id, "https://t.me/store3hunna/45")
            bot.send_message(message.chat.id, "https://t.me/store3hunna/49")
            bot.send_message(message.chat.id, "https://t.me/store3hunna/50")

        elif message.text == 'Аксессуары 💍':
            bot.send_message(message.chat.id, "https://t.me/store3hunna/24")
            bot.send_message(message.chat.id, "https://t.me/store3hunna/25")

        elif message.text == 'Платья 👗':
            bot.send_message(message.chat.id, "https://t.me/store3hunna/33")

        elif message.text == 'Куртки 🧥':
            bot.send_message(message.chat.id, "https://t.me/store3hunna/27")

        elif message.text == 'Штаны 👖':
            bot.send_message(message.chat.id, "https://t.me/store3hunna/20")
            bot.send_message(message.chat.id, "https://t.me/store3hunna/41")
######################################################################################
        else:
            bot.send_message(message.chat.id, "Не опознанная команда, попробуй ещё раз!")



bot.polling()
