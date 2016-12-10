'''Простой бот для telegram.'''
#import python_telegram_bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from getans import get_ans, rand_positive


def talk_to_me(bot, update):
    '''Обработка реплики пользователя.'''
    print('Пришло сообщение:{}'.format(update.message.text))
    ans = get_ans(update.message.text, rand_positive())
    print(ans)
    bot.sendMessage(update.message.chat_id, ans)

def show_error(bot, update, error):
    '''Вывод сообщения об ошибке.'''
    print('bot {} update "{}" error "{}"'.format(bot, update, error))

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
    '''
    bot.sendMessage(update.message.chat_id, text=command_info)


def word_counter(msg_text):
    print('word_counter', msg_text)
    begin_index = msg_text.find('"')
    if begin_index == -1:
        return 'Надо было ввести слова в кавычках'

    end_index = msg_text.rfind('"')
    if begin_index == end_index or begin_index + 1 == end_index:
        return 'Надо было ввести слова в кавычках'

    user_words = msg_text[begin_index + 1:end_index].strip()
    user_words = user_words.strip()
    splited = user_words.split(' ')
    w_count = 0
    for i in splited:
        if i != ' ' and i != '':
            w_count += 1
    if not w_count:
        return 'в кавычках должны были быть слова'
    return 'Количество введенных слов {}'.format(w_count)

def word_count(bot, update):
    '''Считаем количество слов переданных пользователем.'''
    print('Вызван /wordcount')
    print(type(bot))
    print(type(update))
    bot.sendMessage(update.message.chat_id, text=word_counter(update.message.text))

def main():
    '''Главная функция.'''
    updater = Updater('312255597:AAHeQ-xtkTqSUMpNW08TXhFPLeaQtQGE5D4')
    updater.dispatcher.add_handler(CommandHandler("start", greet_user))
    updater.dispatcher.add_handler(CommandHandler("wordcount", word_count))
    updater.dispatcher.add_handler(MessageHandler([Filters.text], talk_to_me))
    updater.dispatcher.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
#    print(word_counter(input('введите текст в кавычках разделенный пробелами: ')))
