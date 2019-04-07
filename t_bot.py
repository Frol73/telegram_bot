# -*- coding: utf-8 -*-
import os
import telebot

from dotenv import load_dotenv

dotenv_path = os.path.dirname(__file__) + "/../configs/env"
load_dotenv(dotenv_path)

bot = telebot.TeleBot(os.environ["token"])

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)