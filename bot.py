import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from info import bot_responses, questions, correct_answers
from data import load_user_data, save_user_data

token = '6453346324:AAFEVDOiWZZn158uhHLVfy5EQb1K228YKQY'
bot = telebot.TeleBot(token=token)

data_path = 'users.json'
user_data = load_user_data(data_path)

user_answers = []
current_question = 0

markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(KeyboardButton('Да'))
markup.add(KeyboardButton('Нет'))


@bot.message_handler(commands=['start'])
def say_start(message):
    bot.send_message(message.chat.id, f"{random.choice(bot_responses['hello'])}.\n"
                                      f"Ты попал на тест по базовому Python. \n"
                                      f"Для полного ознакомления с ботом напишите команду: /help\n"
                                      f"Для начала теста введите команду /test")


@bot.message_handler(commands=['help'])
def say_help(message):
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}! \n"
                                      f"Я бот анкета, которая помогает тебе узнать твой уровень владения языком Python.\n"
                                      f"В конеце теста ты узнаешь свой уровень ззнания Python в балах, "
                                      f"а также получишь соответсвующую картинку. \n"
                                      f"Если будешь готов узнать свои знания языка, воспользуйся командой /test")


@bot.message_handler(commands=['test'])
def create_user(message):
    user_id = str(message.from_user.id)
    if user_id not in user_data:
        user_data[user_id] = {}
        user_data[user_id]['username'] = message.from_user.first_name
        user_data[user_id]['test_points'] = 0
        save_user_data(user_data, data_path)
    elif user_id in user_data:
        bot.send_message(message.chat.id,
                         f"{message.from_user.first_name} рад вас снова видеть!")
    start_test(message)


def start_test(message):
    global user_answers, current_question
    user_answers = []
    current_question = 0
    send_question(message.chat.id)


def send_question(chat_id):
    bot.send_message(chat_id, questions[current_question]["question"], reply_markup=markup)


@bot.message_handler(content_types=['text'])
def handle_answer(message):
    global user_answers, current_question

    if current_question < len(questions):
        user_answers.append(message.text)
        current_question += 1
        if current_question < len(questions):
            send_question(message.chat.id)
        else:
            finish_test(message)
    else:
        bot.send_message(message.chat.id, "Тест уже завершен. Напишите /test, чтобы начать тест заново.")


def finish_test(message):
    global user_answers, correct_answers
    user_id = str(message.from_user.id)

    score = sum(1 for user, correct in zip(user_answers, correct_answers) if user == correct)
    bot.send_message(message.chat.id, f"Тест завершен!\nВаш результат: {score} из {len(questions)}.")

    user_data[user_id]['test_points'] = score
    save_user_data(user_data, data_path)
    send_score(message, score)


def send_score(message, score):
    try:
        if 0 <= score < 3:
            bot.send_message(message.chat.id, 'Очень слабо!')
            bot.send_photo(message.chat.id, open(bot_responses["images"][0], "rb"))
        elif 3 <= score < 6:
            bot.send_message(message.chat.id, 'Я ожидал от тебя большего...')
            bot.send_photo(message.chat.id, open(bot_responses["images"][1], "rb"))
        elif 6 <= score < 9:
            bot.send_message(message.chat.id, 'Тебе нужно подтянуть свои знания по языку')
            bot.send_photo(message.chat.id, open(bot_responses["images"][2], "rb"))
        elif 9 <= score < 12:
            bot.send_message(message.chat.id, 'Довольно не плохо')
            bot.send_photo(message.chat.id, open(bot_responses["images"][3], "rb"))
        elif score == 12:
            bot.send_message(message.chat.id, 'Да ты магистр языка!!!')
            bot.send_photo(message.chat.id, open(bot_responses["images"][4], "rb"))
    except:
        bot.send_message(message.chat.id, f"Ивините за неполадки, на данный момент картинка не доступна. "
                                          f"Уже решаем эту проблему!")


bot.polling()
