# -*- coding: utf-8 -*-
from telegram.ext import Updater         # пакет называется python-telegram-bot, но Python-
from telegram.ext import CommandHandler  # модуль почему-то просто telegram ¯\_(ツ)_/¯

TOKEN = '772289382:AAGC8nQkOxRQNek3glaWe1m-XuLXIh0ibVg'

def start(bot, update):
    # подробнее об объекте update: https://core.telegram.org/bots/api#update
    bot.sendMessage(chat_id=update.message.chat_id, text="Здравствуйте.")

updater = Updater(token=TOKEN)  # тут токен, который выдал вам Ботский Отец!

start_handler = CommandHandler('start', start)  # этот обработчик реагирует
                                                # только на команду /start

updater.dispatcher.add_handler(start_handler)   # регистрируем в госреестре обработчиков
updater.start_polling() 
