import telebot
import os
from youtube_dl_back import downloadVideo
from dotenv import load_dotenv

load_dotenv('example.env')
API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(content_types=['text'])
def test(message):
    url = message.text
    video = open(downloadVideo(url), 'rb')
    chat_id = message.chat.id
    bot.send_document(chat_id=chat_id, document=video,timeout=10000)


bot.infinity_polling()