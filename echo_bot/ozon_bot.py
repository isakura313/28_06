import telebot
token = '1198556805:AAHqX6Ewt_LaryU3aNhVQuOf5TAWOmIQ9Ic'
import random

divizi = ["Ozon такой хороший", "как же я люблю Озон", "Всегда только там заказываю"]
emoji = ['👍', '😊', '🔥', '❤️']

bot = telebot.TeleBot(token)
@bot.message_handler(content_types=["text"])
def repeat_ozon_message(message):
    if message.text == "Ozon":
        message.text = random.choice(divizi)
        bot.send_message(message.chat.id, message.text)
    else:
        message.text = random.choice(emoji)
        bot.send_message(message.chat.id, message.text)

bot.infinity_polling()