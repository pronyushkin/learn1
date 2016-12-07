#import python_telegram_bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from getans import get_ans,rand_positive


def talk_to_me( bot, update ):
	print('Пришло сообщение:{}'.format(update.message.text))
	ans = get_ans( update.message.text, rand_positive )
	bot.sendMessage(update.message.chat_id, ans)

def show_error(bot, update, error):
	print('update "{}" error "{}"'.format(update,error))

def greet_user(bot, update):
    print('Вызван /start')
    print(type(bot))
    print(type(update))
    print(update.message)
    bot.sendMessage(update.message.chat_id, text='Скажи что нибудь')

def main():
	updater = Updater('312255597:AAHeQ-xtkTqSUMpNW08TXhFPLeaQtQGE5D4')
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))
	dp.add_handler(MessageHandler([Filters.text], talk_to_me))
	dp.add_error_handler(show_error)
	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
    main() 