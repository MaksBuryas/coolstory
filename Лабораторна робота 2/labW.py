import telebot
#Доступ к данному боту в телеграмм @neverbot

bot = telebot.TeleBot('1315764944:AAGZ8hJ23idvi1i-vxdDYkzW9gIhEmrx4YE')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Кто создал?' , 'Все!')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Команда старт позволяет работать с клавиатурой', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'кто создал?':
        bot.send_message(message.chat.id, 'Мой создатель Буряс Максим')
    elif message.text.lower() == 'все!':
        bot.send_message(message.chat.id,  'Спасибо что использовали моего бота')


bot.polling()
