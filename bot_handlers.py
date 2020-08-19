import telebot
import pyowm
from bot import bot, owm
from messages import HELLO_MESSAGE, HELP_MESSAGE


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, messages.HELLO_MESSAGE)


@bot.message_handler(commands=['help'])
def send_help(message):
	bot.send_message(message.chat.id, messages.HELP_MESSAGE)

@bot.message_handler(content_types=['text'])
def send_echo(message):
	citty = message.text
	listCity = ['Minsk', 'London', 'Moscow', 'New York', 'Tel Aviv', 'Warsaw', 'Los Angeles', 'San Francisco', 'Toronto', 'Kyiv', 'Paris', 'Prague', 'Sofia', 'Budapest', 'Cairo', 'Istanbul', 'Amsterdam', 'Oslo', 'Stockholm', 'Samara', 'Saint Petersburg', 'Barcelona', 'Madrid', 'Shanghai', 'Hong Kong', 'Wuhan', 'Beijing', 'Seattle', 'Boston']
	if citty in listCity:
		observation = owm.weather_at_place(citty)
		w = observation.get_weather()
		temp = w.get_temperature('celsius')["temp"]
		answer = "In city " + message.text + " now " + w.get_detailed_status() + "\n"
		answer += "Temperature now in range " + str(int(temp)) + "\n\n"
		bot.send_message(message.chat.id, answer)
	else:
		pass


if __name__ == '__main__':
	bot.polling(none_stop=True)