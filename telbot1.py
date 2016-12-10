'''Простой бот для telegram.'''
#import python_telegram_bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
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
        return 'Введите выражение вида 1+2='

    match_result = re.match('(\D*)(\d*)([+,*])(\d*)=', msg_text)
    if not match_result:
        return 'Введите выражение вида 1+2='

    exp_result = None
    try:
        if match_result.group(3) == '+':
            exp_result = int(match_result.group(2)) + int(match_result.group(4))
        elif match_result.group(3) == '*':
            exp_result = int(match_result.group(2)) * int(match_result.group(4))
        elif match_result.group(3) == '/':
            exp_result = int(match_result.group(2)) / int(match_result.group(4))
        elif match_result.group(3) == '-':
            exp_result = int(match_result.group(2)) - int(match_result.group(4))
        else:
            return 'Ошибка программиста сюда попасть не должны'
    except TypeError:
        return 'Неподдерживаемый тип'

    if exp_result:
        return 'Результат подсчета:{}'.format(exp_result)

    return 'Не удалось вычислить результат выражения [{}]'.format(msg_text)

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
    bot.sendMessage(update.message.chat_id, text=calc_from_message(update.message.text))

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
