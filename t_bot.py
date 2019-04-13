# -*- coding: utf-8 -*-
import telebot

from helpers.get_env_data import GetData


def main():
    bot = telebot.TeleBot(GetData.get_token())

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if "Привет" in message.text:
            #bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")  # Для ответа только в лс
            bot.send_message(message.chat.id, f"Привет тебя завут {message.from_user.username}")
        elif message.text == "/help":
            #bot.send_message(message.from_user.id, "Напиши привет") # Для ответа только в лс
            bot.send_message(message.chat.id, "Напиши привет")
        else:
            #bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.") # Для ответа только в лс
            bot.send_message(message.chat.id, "Я тебя не понимаю. Напиши /help.")

    bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    main()
