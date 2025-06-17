import os
import telebot
import datetime
import json
from telebot import types

bot = telebot.TeleBot(os.getenv("TG_TOKEN"))
DATA_FILE_PATH = "sleepy_bot_data.json"
try:
    with open(DATA_FILE_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
except FileNotFoundError:
    data = {}


def write_data_into_file(recorded_data: dict, file_path=DATA_FILE_PATH):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(recorded_data, file, ensure_ascii=False, indent=4, default=str)

def create_record(start_time):
    record = {
        "start_time": start_time,
        "duration": 0,
        "quality": None,
        "notes": None
    }
    return record

def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds % 3600) // 60
  seconds = seconds % 60
  return f"{hours} часов, {minutes} минут и {seconds} секунд"


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Привет! Я буду помогать тебе отслеживать параметры сна. Используй команды /sleep, /wake, /quality, /notes.")


@bot.message_handler(commands=["sleep"])
def sleep(message):
    current_time = datetime.datetime.now()
    user_id = str(message.from_user.id)
    if user_id not in data:
        data[user_id] = []
    data[user_id].append(create_record(current_time))
    write_data_into_file(data)
    bot.reply_to(message, "Спокойной ночи! Не забудь сообщить мне, когда проснёшься, командой /wake.")


@bot.message_handler(commands=["wake"])
def wake(message):
    current_time = datetime.datetime.now()
    user_id = str(message.from_user.id)
    if user_id not in data or data[user_id][-1]["duration"] != 0:
        bot.reply_to(message, "Я не вижу, что ты сообщил мне о начале сна. Используй команду /sleep.")
    else:
        data[user_id][-1]["duration"] = (current_time - data[user_id][-1]["start_time"]).seconds
        write_data_into_file(data)
        sleep_duration = convert_seconds(data[user_id][-1]["duration"])
        bot.reply_to(message, f"Доброе утро! Ты проспал около {sleep_duration}. Не забудь оценить качество сна командой /quality и оставить заметки командой /notes.")


@bot.message_handler(commands=["quality"])
def quality(message):
    user_id = str(message.from_user.id)
    if (user_id not in data) or (data[user_id][-1]["quality"] is not None and data[user_id][-1]["notes"] is not None):
        bot.reply_to(message, "Я не вижу, что ты сообщил мне о начале сна. Используй команду /sleep.")
    elif data[user_id][-1]["duration"] == 0:
        bot.reply_to(message, "Я не вижу, что ты сообщил мне об окончании сна. Используй команду /wake.")
    elif data[user_id][-1]["quality"] is not None and data[user_id][-1]["notes"] is None:
        bot.reply_to(message, "Ты уже давал оценку этому сну, но ты можешь оставить заметку о своем сне, используй команду /notes.")
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
        buttons = [types.KeyboardButton(str(i)) for i in range(1, 11)]
        markup.add(*buttons)
        bot.reply_to(message, "Оцени свой сон по шкале от 1 (ужасно) до 10 (прекрасно):", reply_markup=markup)
        bot.register_next_step_handler(message, save_quality)

def save_quality(message):
    user_id = str(message.from_user.id)
    try:
        data[user_id][-1]["quality"] = int(message.text)
        write_data_into_file(data)
        bot.reply_to(message, "Спасибо за оценку качества сна!", reply_markup=types.ReplyKeyboardRemove())
        if data[user_id][-1]["notes"] is None:
            bot.send_message(message.chat.id, "Теперь ты можешь оставить заметку о своем сне, используй команду /notes.")
        else:
            bot.send_message(message.chat.id,"Чтобы отметить начало следующего сна, используй команду /sleep.")
    except ValueError:
        bot.reply_to(message, "Оценка сна принимается только в числовом формате, используй команду /quality.", reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(commands=["notes"])
def notes(message):
    user_id = str(message.from_user.id)
    if (user_id not in data) or (data[user_id][-1]["quality"] is not None and data[user_id][-1]["notes"] is not None):
        bot.reply_to(message, "Я не вижу, что ты сообщил мне о начале сна. Используй команду /sleep.")
    elif data[user_id][-1]["duration"] == 0:
        bot.reply_to(message, "Я не вижу, что ты сообщил мне об окончании сна. Используй команду /wake.")
    elif data[user_id][-1]["notes"] is not None and data[user_id][-1]["quality"] is None:
        bot.reply_to(message, "Ты уже оставлял заметку об этом сне, но ты можешь оценить качество сна с помощью команды /quality.")
    else:
        note = message.text.lstrip("/notes ")
        if note == "":
            bot.reply_to(message, "Опиши свой сон:")
            bot.register_next_step_handler(message, save_note)
        else:
            message.text = note
            save_note(message)

def save_note(message):
    user_id = str(message.from_user.id)
    data[user_id][-1]["notes"] = message.text
    write_data_into_file(data)
    bot.reply_to(message, "Заметка успешно сохранена!")
    if data[user_id][-1]["quality"] is None:
        bot.send_message(message.chat.id, "Еще ты можешь оценить качество своего сна, используй команду /quality.")
    else:
        bot.send_message(message.chat.id, "Чтобы отметить начало следующего сна, используй команду /sleep.")


bot.polling(none_stop=True, interval=0)