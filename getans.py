def get_bot_dict():
    return {'привет':'И тебе привет!','как дела': 'лучше всех', 'пока':'увидимся', 'Пока!': 'Баюшки'}

def make_ans( d, s, defans ) :
    return d.get( s, defans )

def get_ans( str ) :
    str = str.lower()
    return make_ans( get_bot_dict(), str, 'даже не знаю' )

def interact_ans() :
    r = ''
    while True :
        r = input(':')
        print(get_ans( r ) )
        if r == 'пока':
            return

           
if __name__ == '__main__':
    interact_ans() 

