'''Работа с if'''

def message_by_age(age):
    '''Сообщение о возрасте.'''
    if age < 0:
        return 'ты пока только в проекте'
    elif age < 3:
        return 'сиди дома с мамой'
    elif age < 7:
        return 'срочно в сад'
    elif age < 17:
        return 'школота'
    elif age < 23:
        return 'в вузе учишься?'
    elif age < 65:
        return 'дай денег'
    else:
        return 'отдыхай уже'

def cmd_age():
    '''Команда возраст.'''
    age = input('введите возраст:')
    try:
        age = int(age)
        print(message_by_age(age))
    except ValueError:
        print('возраст должен быть числом')

def learn_strcmp(str1, str2):
    '''Упражнение на сравнение строк.'''
    if str1 == str2:
        return 1
    elif len(str1) > len(str2):
        return 2
    elif str2 == 'learn1':
        return 3
    else:
        return 'результат не предусмотрен заданием'

def cmd_strcmp():
    '''Интерактив для упражнения на стравнение строк.'''
    str1 = input('введите первую строку для сравнения:')
    str2 = input('введите вторую строку для сравнения:')
    ls_result = learn_strcmp(str1, str2)
    print('Результат сравнения:', ls_result)

def cmd_help():
    '''Список допустимых команд.'''
    print('доступные команды:')
    print('\tq - выход')
    print('\t1 - возраст')
    print('\t2 - сравнение строк')

def main():
    '''Главная функция.'''
    cmd_help()
    cmd = ''
    while cmd != 'q':
        cmd = input('введите команду (q/1/2)')
        if cmd == '1':
            cmd_age()
        elif cmd == '2':
            cmd_strcmp()
        else:
            cmd_help()


if __name__ == '__main__':
    main()
