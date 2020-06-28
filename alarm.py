import logging
from telegram.ext import Updater, CommandHandler

# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
#
# logger = logging.getLogger((__name__))

def start(update, context):
    update.message.reply_text('Привет! Используй /set <seconds>, чтобы поставить таймер!')

def alarm(context):
    job = context.job
    context.bot.send_message(job.context, text = "⏰⏰⏰⏰⏰⏰⏰⏰⏰")

def set_timer(update, context):
    """ Добавляем занятие для нашего бота в очередь"""
    chat_id = update.message.chat_id
    try:
        due = int(context.args[0])
        if due < 0:
            update.message.reply_text("Нельзя ставить отрицательные значения! ")
            return
        #Добавляем наше дело в очередь и обнуляем сроки, если есть один такой
        if 'job' in context.chat_data:
            old_job = context.chat_data['job']
            old_job.schedule_removal()
        new_job = context.job_queue.run_once(alarm, due, context = chat_id)
        context.chat_data['job'] = new_job

        update.message.reply_text("Таймер был успешно установлен")
    except(IndexError, ValueError):
        update.message.reply_text('Использование: /set <seconds>')

def main():
    """ Запуск нашего бота"""
    #Создаем экземпляр Update и передаем туда токен нашего пользователя
    updater = Updater('1198556805:AAHqX6Ewt_LaryU3aNhVQuOf5TAWOmIQ9Ic', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(CommandHandler("set", set_timer, pass_args=True,
                                                    pass_job_queue=True,
                                                    pass_chat_data=True ))

    updater.start_polling()
    updater.idle()

main()
