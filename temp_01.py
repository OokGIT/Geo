import telebot
from geopy.point import *


bot = telebot.TeleBot("1166720116:AAGgoMXigeV7vp0LoPzMXr_G_2o9ntx5Kks")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	# bot.reply_to(message, message.text)
	coords = message.text
	reg_geo = Point(coords).format_decimal().replace(' ', '')
	result = [float(val) for val in reg_geo.split(',')]
	lat1 = (result[0])
	lon1 = (result[1])
	print(lat1)
	print(lon1)


bot.infinity_polling(skip_pending=True)  # Skip pending skips old updates
