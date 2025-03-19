import telebot
import requests

bot = telebot.TeleBot('6728445824:AAG6Kv2h2R7_gCdlh8XkBWBbAQUKUokYKOs')
API_KEY = '2ff7e3e1de4c5d4e99e4a79f2ce81012'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hallo, ich bin ein Wetter-Bot. Sag mir den Namen einer Stadt und ich werde dir sagen, wie das Wetter dort momentan ist.')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Hilfe-Informationen:')


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, 'Info: Dies ist ein Telegram-Bot, der ausschließlich dazu dient, die Temperatur in Städten weltweit anzuzeigen. Der Bot wurde von einem Anfänger erstellt, deshalb kann der Bot momentan nur auf die Befehle /start, /help und /info reagieren und das Wetter in der angegebenen Stadt anzeigen.')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        bot.reply_to(message, f'Momentan in der Stadt {city.capitalize()}:\nTemperatur: {temp}°C\nGefühlt wie: {feels_like}°C\nMinimale Temperatur: {temp_min}°C\nMaximale Temperatur: {temp_max}°C')
    else:
        bot.reply_to(message, 'Ups! Etwas ist schief gelaufen. Überprüfe die Schreibweise der Stadt und versuche es noch einmal.')

bot.polling(none_stop=True)

