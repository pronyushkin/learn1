import random

def get_bot_dict():
    return {    
    'привет':'И тебе привет!',
    'как дела': 'лучше всех', 
    'пока':'увидимся', 
    'пока!': 'Баюшки'
    }

def make_ans( d, s, defans ) :
    return d.get( s, defans )

def get_ans( str, defans = 'даже не знаю' ) :
    str = str.lower()
    return make_ans( get_bot_dict(), str, defans )

def rand_positive( deftext = 'даже не знаю' ) :
    l = [
    'Ты мой котик',
    'Ты мой бедный зайчик!',
    'Это просто день такой. Все наладится, увидишь!',
    'Это просто год такой. Все наладится, увидишь!',
    'Ай-ай-ай, Ну как же так? (((',
    'Иди скорей на ручки!',
    'Дай обниму!',
    'Ты лучше всех!',
    'Ты моя умница! Не расстраивайся, завтра всё будет хорошо.',
    'Скушай тортик :)'
    ]

    i = random.randrange(0,len(l) + 1 )
    if i < len(l) :
        return l[i]
    return deftext



def interact_ans() :
    r = ''
    while True :
        print( rand_positive() )
        r = input(':')
        print(get_ans( r ) )
        if r == 'пока':
            return

           
if __name__ == '__main__':
    interact_ans() 

