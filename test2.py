from  math import sqrt

def do_nothing() :
    return None


def test_info() :
    user_info = { 'first_name':'fn','last_name':'ln'}
    print(user_info['first_name'], user_info['last_name'])
    print('словарь: ', user_info)
    user_info['first_name'] = input('введите имя: ') 
    user_info['last_name' ] = input('введите фамилию: ' )
    print('имя: ', user_info['first_name'])
    print('фамилия: ', user_info['last_name'])
    print('словарь: ', user_info)   

def interact_sqrt() :
    print( 'решение квадратного уравнения' )
    a = int( input('введите коэффициетн A:' ) )
    b = int( input('введите коэффициетн B:' ) )
    c = int( input('введите коэффициетн C:' ) )
    copmute_sqrt( a, b, c)

def copmute_sqrt( a, b, c) :
    if a == 0:
        print('x = ', -c/b)
    else :
        d = b * b - 4 * a * c
        if d < 0 :
            print('нет действительных корней' )
        elif d == 0:
            print('x = ', -b/(2*a))
        else :
            print('x1 = ', (-b + sqrt(d) ) /(2*a))
            print('x1 = ', (-b - sqrt(d) ) /(2*a))

def get_ans( d, s, defans ) :
    return d.get( s, defans )


def interact_ans() :
    d = {'привет':'И тебе привет!','как дела': 'лучше всех', 'пока':'увидимся'}
    r = ''
    while True :
        r = input(':')
        r = r.lower()
        print(get_ans( d, r, 'даже не знаю' ))
        if r == 'пока':
            return

           
if __name__ == '__main__':
    interact_sqrt() 

