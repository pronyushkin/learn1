#import python_telegram_bot
from telegram.ext import Updater, CommandHandler

def greet_user(bot, update):
    print('Вызван /start')

def main():
	updater = Updater('312255597:AAHeQ-xtkTqSUMpNW08TXhFPLeaQtQGE5D4')
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))
	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
    main() 