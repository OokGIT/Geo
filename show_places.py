import csv
import mpu
import telebot

bot = telebot.TeleBot("2042323681:AAGlGm683i4jAEEFoatxZl9tpUzfZCtlruo", parse_mode=None)

lat1 = 50.44029
lon1 = 30.55950
min_geo_range = 30
max_geo_range = 50

rows = {}
file = open('ua-list.csv', 'r', encoding='windows-1251')
csv_reader = list(csv.reader(file, delimiter=';'))
for elem in csv_reader:
    distance = mpu.haversine_distance((lat1, lon1),
                                      (float(elem[4]), float(elem[3])))
    rows[elem[2]] = distance
file.close()
sorted_rows = dict(sorted(rows.items(), key=lambda x: x[1]))
final_dict = {}
for k, v in sorted_rows.items():
    if min_geo_range <= v <= max_geo_range:
        final_dict[k] = round(v, 1)

final_string = ("\n".join("{!r} - {!r}".format(k, v)
                          for k, v in final_dict.items())).replace("'", "").replace('"', '')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, final_string)


bot.infinity_polling()
