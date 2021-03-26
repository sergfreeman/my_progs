import telebot
import config

class CalcuBotOr:
    check_operation = 0
    def dialogue(self):
        bot = telebot.TeleBot(config.token)

        @bot.message_handler(content_types='text')
        def write_text(message):
            if chec
            bot.send_message(message.chat.id,"""
                           Оберіть арифметичну дію:
                           -
                           +
                           /
                           *
                                               """)
            # bot.send_message('text', 'Привіт')
            if message.text == '1':
                bot.send_message(message.chat.id, 'Hello, my friend!')



            if message.text == '+':
                pass

        bot.polling()

cb = CalcuBotOr()
cb.dialogue()
