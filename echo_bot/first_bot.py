import telebot
token = '1198556805:AAHqX6Ewt_LaryU3aNhVQuOf5TAWOmIQ9Ic'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_message(message):
    bot.send_message(message.chat.id, message.text)

bot.infinity_polling()