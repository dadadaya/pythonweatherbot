import pyTelegramBotAPI
import pyowm
import config


bot = telebot.Telebot(config.TOKEN)
owm = pyowm.OWM(config.WEATHERTOKEN, language = "en")
