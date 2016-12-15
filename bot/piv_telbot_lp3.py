'''Простой бот для telegram написан в рамках прохождения курся learn python 3.'''
#import python_telegram_bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
#мои модули
from piv_getans import get_ans, rand_positive
from piv_calc import calc_from_words_message
from piv_wordcount import word_counter

def show_error(bot, update, error):
    '''Вывод сообщения об ошибке.'''
    print('bot {} update "{}" error "{}"'.format(bot, update, error))

def text_handler(bot, update,):
    '''Обработка реплики пользователя.'''
    print('Пришло сообщение:{}'.format(update.message.text))
    ans = get_ans(update.message.text, rand_positive())
    print(ans)
    bot.sendMessage(update.message.chat_id, ans)




def cmd_word_count(bot, update):
    '''Обработка команды на подсчет слов.'''
    print('Вызван /wordcount')
    print(type(bot))
    print(type(update))
    bot.sendMessage(update.message.chat_id, text=word_counter(update.message.text))

#todo обработчики довольно одинаковы надо сделать один
def cmd_calc(bot, update):
    '''Обработчик команда на вычисление результата простого выражения /calc.'''
    print('Вызван /calc')
    print(type(bot))
    print(type(update))
    print(update.message)
    calc_keyboard = [['0','1','2','3','4'],['5','6','7','8','9'], ['+','-','*','/','=']]
    reply_markup = ReplyKeyboardMarkup(calc_keyboard)
    bot.sendMessage(update.message.chat_id, text='Калькулятор', reply_markup=reply_markup)    
    bot.sendMessage(update.message.chat_id, text=calc_from_words_message(update.message.text))

def cmd_start(bot, update,chat_data):
    '''Приветствие пользователя по команде /start.'''
    print('Вызван /start')
    print(type(bot))
    print(type(update))
    print(update.message)
    chat_data['cmd'] = ''
    command_info = '''
    Доступны следующие команды:
    /start - эта информация
    /wordcount [слова в кавычках разделенные пробелом] - подсчитает количество введенных слов
    /calc - начать вычисление простых примеров вида 1+2=  
            т.е. два числа операция и равно в конце, пробелы не допустимы            
    /cities - начать игру в города 
    также можно просто что нибудь написать и тогда я что то отвечу
    '''
    bot.sendMessage(update.message.chat_id, text=command_info)


def main():
    '''Главная функция.'''
    updater = Updater('312255597:AAHeQ-xtkTqSUMpNW08TXhFPLeaQtQGE5D4')
    updater.dispatcher.add_handler(CommandHandler('start', cmd_start, pass_chat_data=True))
    updater.dispatcher.add_handler(CommandHandler('wordcount', cmd_word_count, pass_args=True, pass_chat_data=True))
    updater.dispatcher.add_handler(CommandHandler('calc', cmd_calc, pass_args=True, pass_chat_data=True))
    updater.dispatcher.add_handler(MessageHandler([Filters.text], text_handler, pass_args=True, pass_chat_data=True))
    updater.dispatcher.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
   main()
