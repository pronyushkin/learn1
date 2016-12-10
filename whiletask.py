'''Задание на работу с циклами'''
import getans
from getans import get_ans

def cmd_help():
    '''Вывод списка команд'''
    print('доступные команды:')
    print('\tq - выход')
    print('\t1 - поиск имени в списке')
    print('\t2 - как дела')
    print('\t3 - бот')


def find_person( l, name ):
    '''Поиск в списке с удалением'''
    while l:
        if l.pop() == name:
            print(name,'найден')
            return 
    print(name,' не найден')

def cmd_findname():
    '''Команда на поиск в списке'''
    l = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
    name = 'Валера'
    print( 'Ищем ',name ,' в списке:', l ) 
    find_person( l, name )

def ask_user():
    '''Опрос пользователя'''
    ans = ''
    try:
        while not ans == 'Хорошо':
            ans = input('Как дела? ')
        print('так держать')
    except KeyboardInterrupt:
        print('ну и ладно')

def cmd_bot():
    '''Простой консольный бот'''
    ans = ''
    while not ans == 'Пока!':
        ans = input('Как дела?')
        print(get_ans(ans))

def main():
    cmd_help()
    cmd = ''
    while not cmd == 'q':
        cmd = input('введите команду (q)')
        if cmd == '1':
            cmd_findname()
        elif cmd == '2':
            ask_user()
        elif cmd == '3':
            cmd_bot()
        else :
            cmd_help()


if __name__ == '__main__':
    main() 
