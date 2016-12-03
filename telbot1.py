#import python_telegram_bot
from telegram.ext import Updater

def main():
	updater = Updater('312255597:AAHeQ-xtkTqSUMpNW08TXhFPLeaQtQGE5D4')
	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
    main() 