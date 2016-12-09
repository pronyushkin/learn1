'''Еще набор тестовых заданий с интенсива.'''
from  math import sqrt

def do_nothing():
    '''Делаем ничего, возвращаем ничто.'''
    return None


def test_info():
    '''Тест работа со словарем.'''
    user_info = {'first_name':'fn', 'last_name':'ln'}
    print(user_info['first_name'], user_info['last_name'])
    print('словарь: ', user_info)
    user_info['first_name'] = input('введите имя: ')
    user_info['last_name'] = input('введите фамилию: ')
    print('имя: ', user_info['first_name'])
    print('фамилия: ', user_info['last_name'])
    print('словарь: ', user_info)

def interact_sqrt():
    '''Задание решение квадратного уравнения.'''
    print('решение квадратного уравнения')
    ratio_a = int(input('введите коэффициетн A:'))
    ratio_b = int(input('введите коэффициетн B:'))
    ratio_c = int(input('введите коэффициетн C:'))
    compute_sqrt(ratio_a, ratio_b, ratio_c)

def compute_sqrt(ratio_a, ratio_b, ratio_c):
    '''Решение квадратного уравнения.'''
    if ratio_a == 0:
        print('x = ', -ratio_c/ratio_b)
    else:
        the_discriminant = ratio_b * ratio_b - 4 * ratio_a * ratio_c
        if the_discriminant < 0:
            print('нет действительных корней')
        elif the_discriminant == 0:
            print('x = ', -ratio_b/(2*ratio_a))
        else:
            print('x1 = ', (-ratio_b + sqrt(the_discriminant)) /(2*ratio_a))
            print('x1 = ', (-ratio_b - sqrt(the_discriminant)) /(2*ratio_a))

def get_ans(ans_dict, user_in, defans):
    '''Ответ по словарю.'''
    return ans_dict.get(user_in, defans)


def interact_ans():
    '''Консольный бот.'''
    rep_dict = {'привет':'И тебе привет!', 'как дела': 'лучше всех', 'пока':'увидимся'}
    user_in = ''
    while True:
        user_in = input(':')
        user_in = user_in.lower()
        print(get_ans(rep_dict, user_in, 'даже не знаю'))
        if user_in == 'пока':
            return


if __name__ == '__main__':
    interact_ans()
