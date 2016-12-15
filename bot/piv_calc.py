'''Простой калькулятор.'''
import re

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


if __name__ == '__main__':
#    print(calc_from_message(input('введите выражение вида 1+2=: ')))
    print(calc_from_words_message(input('введите выражение вида 1+2=: ')))