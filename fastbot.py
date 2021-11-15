import telebot
from telebot.types import Message

bot = telebot.TeleBot('2128027585:AAERhVZomoL8FkQsg9FNUgXE7n2pIbSCw50')


@bot.message_handler(commands=['start', 'help'])
def welcome_message(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    buttonNOT = telebot.types.KeyboardButton('Пошел нахуй')
    markup.row(buttonNOT, buttonNOT)
    bot.send_message(message.chat.id, 'Долбаеб, че за хуйню ты мне отправил? Не видишт клавишу снизу?', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def message1(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    if message.text.replace(' ','') == 'Пошелнахуй' or message.text.replace(' ', '') == 'пошелнахуй' or message.text.replace(' ', '') == 'пошёлнахуй' or message.text.replace(' ', '') == 'Пошёлнахуй':
        bot.send_message(message.chat.id, 'Сам пошел нахуй')
        buttonNOT = telebot.types.KeyboardButton('Пошел нахуй')
        markup.row(buttonNOT)
    else:
        bot.send_message(message.chat.id, 'Долбаеб, че за хуйню ты мне отправил? Не видишт клавишу снизу?')
        buttonNOT = telebot.types.KeyboardButton('Пошел нахуй')
        markup.row(buttonNOT, buttonNOT)


bot.polling()