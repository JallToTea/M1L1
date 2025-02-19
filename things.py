import telebot
from bot_logic import gen_pass
from bot_logic import gen_prot
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7714188158:AAG6k2gwV21Wh3vLTruWh01A6jh3gZPNy3w")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['password'])
def send_password(message):
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(commands=['prophet'])
def send_pred(message):
    bot.reply_to(message, gen_prot())

@bot.message_handler(commands=['help'])
def send_pred(message):
    bot.reply_to(message, "Вот список команд, которые умеет этот бот: /start, /hello, /bye, /password, /prophet, /help")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
