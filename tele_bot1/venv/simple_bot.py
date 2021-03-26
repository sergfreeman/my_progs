import telebot
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types='text')
def write_text(message):
    if message.text == 'Hi':
        bot.send_message(message.chat.id, 'Hello, my friend!')


bot.polling()