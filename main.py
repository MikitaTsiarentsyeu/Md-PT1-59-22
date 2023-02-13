import pyowm
import telebot
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM('1a28208731e07aec35dc3883f8cfe5e7', config_dict)
bot = telebot.TeleBot("5838712628:AAG6_Aoic8smlAfKQrk4Ifr_IYL6BQlwaiw", parse_mode=None)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Введите название города:\n")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
   try:
      mgr = owm.weather_manager()
      observation = mgr.weather_at_place(message.text)
      w = observation.weather
      weather_info = "В городе "+message.text+" сейчас "+w.detailed_status+"\n"
      weather_info += "Температура: " + str(w.temperature('celsius')['temp'])+"\n"
      weather_info += "Влажность: " + str(w.humidity())+"\n"
      weather_info += "Скорость ветра: " + str(w.wind()['speed'])+"\n"
      bot.reply_to(message, weather_info)
   except Exception:
        bot.reply_to(message, 'Ошибка! Город не найден.')
bot.polling(none_stop=True)



