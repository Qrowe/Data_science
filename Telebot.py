import telebot
import random
bot = telebot.TeleBot('956160046:AAGlAqCOx5tA8ckDvePlVOr3MgZ950OJVjk')

@bot.message_handler(content_types=['text'])

def get_text_messages(message):

    # Если написали «Привет»

    if message.text == "Привет":

        # Пишем приветствие

        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")

bot.polling(none_stop=True, interval=0)


