import telegram
from PIL import Image, ImageGrab

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import re
import time
token = '' #Input your token here


def start(bot, update):
    bot.send_message(update.message.chat_id, text="Добро пожаловать!")
    bot.send_message(update.message.chat_id, text="Введите код") 
def answer(bot, update):
    if update.message.text=="":   # Print here your pin
        bot.send_message(update.message.chat_id, text="Удачно!")
        img = ImageGrab.grab()
        img.save("", "JPEG")   #Print route to folder. It should be the same as where screenhot_bot.py is located
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open('temp_screen.jpg', 'rb'))
        bot.send_message(update.message.chat_id, text="Температура")
    else:
        bot.send_message(update.message.chat_id, text="Ошибка!")



    
def main():

    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    #dp.add_handler (CallbackQueryHandler(button))
    dp.add_handler(MessageHandler([Filters.text], answer))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
