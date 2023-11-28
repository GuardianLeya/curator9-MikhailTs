import telebot

bot1 = telebot.TeleBot('6827958616:AAF3QUSBzPZSCsLfwyg05VktqzBLruHxCT0')


@bot1.message_handler(commands=['start'])
def main(message):
    bot1.send_message(message.chat.id, '*Выбирайте, что вас интересует, из списка* (введите команду /list)', parse_mode='Markdown')

@bot1.message_handler(commands=['list'])
def main(message):
    bot1.send_message(message.chat.id, '[ОСНОВНОЙ ЧАТ](https://t.me/kx_fairway) \n[БОТ ДЛЯ ЗАКАЗОВ](https://t.me/Price_KX_bot) \n[Мой YouTube](https://www.youtube.com/playlist?list=PLO9AVV7Efj7G54paXXgH4ihLNHM45mVx0)', parse_mode='Markdown')


bot1.infinity_polling()