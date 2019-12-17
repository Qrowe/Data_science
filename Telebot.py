import telebot
import random
bot = telebot.TeleBot('токен')

@bot.message_handler(content_types=['text'])

def get_text_messages(message):

    # Если написали «Привет»

    if message.text == "Привет":

        # Пишем приветствие

        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши, привет.')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши /help.')

#готовим кнопки
keyboard = types.InlineKeyboardMarkup()

# По очереди готовим текст и обработчик для каждого знака зодиака

key_oven = types.InlineKeyboardButton(text = 'Овен', callback_data = 'zodiac')
keyboard.add(key_oven)

key_telec = types.InlineKeyboardButton(text = 'Телец', callback_data = 'zodiac')
keyboard.add(key_telec)

key_gemini = types.InlineKeyboardButton(text = 'Близнецы', callback_data = 'zodiac')
keyboard.add(key_gemini)

key_cancer = types.InlineKeyboardButton(text = 'Рак', callback_data = 'zodiac')
keyboard.add(key_cancer)

key_lion = types.InlineKeyboardButton(text = 'Лев', callback_data = 'zodiac')
keyboard.add(key_lion)

key_deva = types.InlineKeyboardButton(text = 'Дева', callback_data = 'zodiac')
keyboard.add(key_deva)

key_vesy = types.InlineKeyboardButton(text = 'Весы', callback_data = 'zodiac')
keyboard.add(key_vesy)

key_scorpion = types.InlineKeyboardButton(text = 'Скорпион', callback_data = 'zodiac')
keyboard.add(key_scorpion)

key_strelec = types.InlineKeyboardButton(text = 'Стрелец', callback_data = 'zodiac')
keyboard.add(key_strelec)

key_kozerog = types.InlineKeyboardButton(text = 'Козерог', callback_data = 'zodiac')
keyboard.add(key_kozerog)

key_vodoley = types.InlineKeyboardButton(text = 'Водолей', callback_data = 'zodiac')
keyboard.add(key_vodoley)

key_ryby = types.InlineKeyboardButton(text = 'Рыбы', callback_data = 'zodiac')
keyboard.add(key_ryby)

bot.polling(none_stop=True, interval=0)

first = ["Сегодня — идеальный день для новых начинаний.","Оптимальный день для того, чтобы решиться на смелый поступок!",
         "Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.",
         "Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.",
         "Плодотворный день для того, чтобы разобраться с накопившимися делами."]

second = ["Но помните, что даже в этом случае нужно не забывать про","Если поедете за город, заранее подумайте про",
         "Те, кто сегодня нацелен выполнить множество дел, должны помнить про","Если у вас упадок сил, обратите внимание на",
         "Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]

second_add = ["отношения с друзьями и близкими.","работу и деловые вопросы, которые могут так некстати помешать планам.",
              "себя и своё здоровье, иначе к вечеру возможен полный раздрай.","бытовые вопросы — особенно те, которые вы не доделали вчера.",
              "отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]

third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.",
         "Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.",
         "Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.",
         "Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.",
         "Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]

print("1 — Овен")

print("2 — Телец")

print("3 — Близнецы")

print("4 — Рак")

print("5 — Лев")

print("6 — Дева")

print("7 — Весы")

print("8 — Скорпион")

print("9 — Стрелец")

print("10 — Козерог")

print("11 — Водолей")

print("12 — Рыбы")

zodiac = int(input('{blue}Введите число с номером знака Зодиака:{endcolor}'.format(blue = '\033[96m', endcolor = '\033[0m')))

if 0 < zodiac < 13:
    print(random.choice(first), random.choice(second), random.choice(second_add), random.choice(third))
else:
    print('Вы ощиблись числом, запустите прогррамму еще раз')


