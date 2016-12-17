'''Простой бот для telegram написан в рамках прохождения курся learn python 3.'''
#import python_telegram_bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, ReplyKeyboardHide
#мои модули
from piv_getans import get_ans, rand_positive
from piv_calc import calc_from_words_message, replace_eq
from piv_wordcount import word_counter

###########################################################
###вспомогательные функции
###########################################################
def reset_chat(bot, update, chat_data, msg_text):
    '''Сброс режима.'''
    print('reset_chat msg_text',msg_text)
    chat_data['cmd'] = ''
    chat_data['expression'] = ''
    chat_data['cities'] = {}
    hide_keyboard = ReplyKeyboardHide()
    print(hide_keyboard)
    bot.sendMessage(update.message.chat_id, text=msg_text, reply_markup=hide_keyboard) 


def text_calc(args_as_str, bot, chat_data, chat_id):
    '''Обработка сообщения для калькулятора.'''
    args_as_str = args_as_str.lower()
    args_as_str = replace_eq(args_as_str)
    print('text_calc', args_as_str)
    if '=' in args_as_str:
        bot.sendMessage(chat_id, text=calc_from_words_message(args_as_str))
    else:
        chat_data['expression'] = chat_data.get('expression', '') + args_as_str


def text_cities(args_as_str, bot, chat_data, chat_id):
    '''
    TODO реализация обработки города введенного пользователем
    '''
    bot.sendMessage(update.message.chat_id, 'Ой я пока не знаю ни одного города. Ты сказал {}'.format(args_as_str))


def show_error(bot, update, error):
    '''Вывод сообщения об ошибке.'''
    print('bot {} update "{}" error "{}"'.format(bot, update, error))


def text_handler(bot, update, chat_data):
    '''Обработка реплики пользователя.'''
    print('Пришло сообщение:{}'.format(update.message.text))
    cmd = chat_data.get('cmd', '')
    if cmd == 'calc':
        text_calc(update.message.text, bot, chat_data, update.message.chat_id)
    elif cmd == 'cities':
        text_cities(update.message.text, bot, chat_data, update.message.chat_id)
    else:
        ans = get_ans(update.message.text, rand_positive())
        print(ans)
        bot.sendMessage(update.message.chat_id, ans)


def cmd_cities(bot, update, args, chat_data):
    '''
    Обработка команды /cities
    Переход в режим игры в города
    '''
    print('Вызван /cities')
    print(type(bot))
    print(type(update))
    print(update.message)
    chat_data['cmd'] = 'cities'
    chat_data['cities'] = {}#TODO сюда надо класть список городов
    reset_chat(bot, update, chat_data, 'Играем в города, начинай!')


def cmd_calc(bot, update, args, chat_data):
    '''
    Обработка команды /calc
    Переход в режим калькулятора и вычисление выражения если оно есть
    '''
    print('Вызван /calc args', args)
    #print(type(bot))
    #print(type(update))
    #print(update.message)
    #print(chat_data)
    #print(args)
    cmd = chat_data.get('cmd', '')
    print('cmd: ', cmd)
    if cmd != 'calc':
        chat_data['cmd'] = 'calc'
        chat_data['expression'] = ''
        calc_keyboard = [['0','1','2','3','4'],['5','6','7','8','9'], ['+','-','*','/','=']]
        reply_markup = ReplyKeyboardMarkup(calc_keyboard, resize_keyboard = True, selective = True)
        bot.sendMessage(update.message.chat_id, text='режим Калькулятор', reply_markup=reply_markup) 
    args_as_str = ' '.join(args)
    args_as_str = replace_eq(args_as_str)
    print('args_as_str:',args_as_str)
    text_calc(args_as_str, bot, chat_data, update.message.chat_id)


def cmd_word_count(bot, update, args, chat_data):
    '''Обработка команды на подсчет слов.'''
    print('Вызван /wordcount')
    print(type(bot))
    print(type(update))
    args_as_str = ' '.join(args)
    reset_chat(bot, update, chat_data,word_counter(args_as_str))


def cmd_start(bot, update, chat_data):
    '''Приветствие пользователя по команде /start.'''
    print('Вызван /start')
    print(type(bot))
    print(type(update))
    print(update.message)
    command_info = '''
    Доступны следующие команды:
    /start - эта информация
    /wordcount [слова в кавычках разделенные пробелом] - подсчитает количество введенных слов
    /calc - начать вычисление простых примеров вида 1+2=  
            т.е. два числа операция и равно в конце, пробелы не допустимы            
    /cities - начать игру в города 
    также можно просто что нибудь написать и тогда я что то отвечу
    '''
    reset_chat(bot, update, chat_data,command_info)


def main():
    '''Главная функция.'''
    botid = ''
    with open('botid.txt', 'r', encoding='utf-8') as f:
        botid = f.read()  
    updater = Updater(botid)
    updater.dispatcher.add_handler(CommandHandler('start',        cmd_start,                      pass_chat_data=True))
    updater.dispatcher.add_handler(CommandHandler('wordcount',    cmd_word_count, pass_args=True, pass_chat_data=True))
    updater.dispatcher.add_handler(CommandHandler('calc',         cmd_calc,       pass_args=True, pass_chat_data=True))
    updater.dispatcher.add_handler(CommandHandler('cities',       cmd_cities,     pass_args=True, pass_chat_data=True))
    updater.dispatcher.add_handler(MessageHandler([Filters.text], text_handler,                   pass_chat_data=True))
    updater.dispatcher.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
   main()
