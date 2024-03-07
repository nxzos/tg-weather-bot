import telebot
import requests

bot = telebot.TeleBot('token for your bot')
API_KEY = 'your API key'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я телеграм бот для погоды. Скажи название какого-нибудь города и я скажу какая там на данный момент погода.')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Help info:')

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, 'Инфо: Это тг бот сделанный исключительно для отслеживания градуса погоды в городах мира. Бот был сделан новичком по этому на данный момент бот умеет только отвечать на команды /start /help и /info и показывать погоду в указаном ему городе.')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    url = 'url of your API key and the name of the city which you gonna choice during process'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        bot.reply_to(message, f'Сейчас в городе {city.capitalize()}:\nТемпература: {temp}°C\nОщущается как: {feels_like}°C\nМинимальная температура: {temp_min}°C\nМаксимальная температура: {temp_max}°C')
    else:
        bot.reply_to(message, 'Упс! Что-то пошло не так. Проверьте правильность написания названия города и попробуйте еще раз.')

bot.polling(none_stop=True)
