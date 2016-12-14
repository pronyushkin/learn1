'''Простой бот для telegram.'''
#import python_telegram_bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
from getans import get_ans, rand_positive
import re

def talk_to_me(bot, update):
    '''Обработка реплики пользователя.'''
    print('Пришло сообщение:{}'.format(update.message.text))
    ans = get_ans(update.message.text, rand_positive())
    print(ans)
    bot.sendMessage(update.message.chat_id, ans)

def show_error(bot, update, error):
    '''Вывод сообщения об ошибке.'''
    print('bot {} update "{}" error "{}"'.format(bot, update, error))

def calc_from_message(msg_text):
    '''Пытаемся обработать строку как калькулятор.
    [1+2=]
    '''
    msg_text = ' ' + msg_text.strip()
    end_index = msg_text.rfind('=')
    if end_index == -1:
        msg_text += '='

    match_result = re.match('(\D*)([\d.]*)([+,*,/,-])([\d.]*)(\D*)', msg_text)
    if not match_result:
        return 'Введите выражение вида 1+2='

    exp_result = None
    try:
        if match_result.group(3) == '+':
            exp_result = float(match_result.group(2)) + float(match_result.group(4))
        elif match_result.group(3) == '*':
            exp_result = float(match_result.group(2)) * float(match_result.group(4))
        elif match_result.group(3) == '/':
            if not int(match_result.group(4)):
                return 'деление на ноль не поддерживается'
            exp_result = float(match_result.group(2)) / float(match_result.group(4))
        elif match_result.group(3) == '-':
            exp_result = float(match_result.group(2)) - float(match_result.group(4))
        else:
            return 'Ошибка программиста сюда попасть не должны'
    except TypeError:
        return 'Неподдерживаемый тип'

    if exp_result:
        if int(exp_result) != exp_result:
            exp_result = round(exp_result, 2)
        return 'Результат подсчета:{}'.format(exp_result)

    return 'Не удалось вычислить результат выражения [{}]'.format(msg_text)

def calc_from_words_message(msg_text):
    '''Пытаемся обработать строку которая может содержать слова вместо цифр.
    [один плюс два]
    '''
    msg_text = msg_text.lower()
    msg_text = msg_text.replace('сколько будет','')
    msg_text = msg_text.replace('один','1')
    msg_text = msg_text.replace('два','2')
    msg_text = msg_text.replace('три','3')
    msg_text = msg_text.replace('четыре','4')
    msg_text = msg_text.replace('пять','5')
    msg_text = msg_text.replace('шесть','6')
    msg_text = msg_text.replace('семь','7')
    msg_text = msg_text.replace('восемь','8')
    msg_text = msg_text.replace('девять','9')
    msg_text = msg_text.replace('десять','10')
    msg_text = msg_text.replace('плюс','+')
    msg_text = msg_text.replace('прибавить','+')
    msg_text = msg_text.replace('минус','-')
    msg_text = msg_text.replace('вычесть','-')
    msg_text = msg_text.replace('отнять','-')
    msg_text = msg_text.replace('умножить на','*')
    msg_text = msg_text.replace('умножить','*')
    msg_text = msg_text.replace('делить на','/')
    msg_text = msg_text.replace('делить','/')
    msg_text = msg_text.replace(':','/')
    msg_text = msg_text.replace('разделить','/')
    msg_text = msg_text.replace('разделить на','/')
    msg_text = msg_text.replace('равно','=')
    msg_text = msg_text.replace('равняется','=')
    msg_text = msg_text.replace(',','.')
    msg_text = msg_text.replace(' и ','.')
    msg_text = msg_text.replace(' ','')
    return calc_from_message(msg_text)


def word_counter(msg_text):
    '''Считаем количество слов.'''
    print('word_counter', msg_text)
    begin_index = msg_text.find('"')
    if begin_index == -1:
        return 'Надо было ввести слова в кавычках'

    end_index = msg_text.rfind('"')
    if begin_index == end_index or begin_index + 1 == end_index:
        return 'Надо было ввести слова в кавычках'

    user_words = msg_text[begin_index + 1:end_index].strip()
    splited = user_words.split(' ')
    w_count = 0
    for i in splited:
        if i != ' ' and i != '':
            w_count += 1
    if not w_count:
        return 'в кавычках должны были быть слова'
    return 'Количество введенных слов {}'.format(w_count)

def word_count(bot, update):
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

def greet_user(bot, update):
    '''Приветствие пользователя по команде /start.'''
    print('Вызван /start')
    print(type(bot))
    print(type(update))
    print(update.message)
    command_info = '''
    Доступны следующие команды:
    /start - эта информация
    /wordcount [слова в кавычках разделенные пробелом] - подсчитает количество введенных слов
    также можно просто что нибудь написать и тогда я что то отвечу
    /calc - вычисление простых примеров вида 1+2=  \nт.е. два числа операция и равно в конце, пробелы не допустимы
    '''
    bot.sendMessage(update.message.chat_id, text=command_info)


def main():
    '''Главная функция.'''
    updater = Updater('312255597:AAHeQ-xtkTqSUMpNW08TXhFPLeaQtQGE5D4')
    updater.dispatcher.add_handler(CommandHandler('start', greet_user))
    updater.dispatcher.add_handler(CommandHandler('wordcount', word_count))
    updater.dispatcher.add_handler(CommandHandler('calc', cmd_calc))
    updater.dispatcher.add_handler(MessageHandler([Filters.text], talk_to_me))
    updater.dispatcher.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
   main()
#    print(word_counter(input('введите текст в кавычках разделенный пробелами: ')))
#    print(calc_from_message(input('введите выражение вида 1+2=: ')))
#    print(calc_from_words_message(input('введите выражение вида 1+2=: ')))