'''Получение ответа для пользователя.'''
import random

def get_bot_dict():
    '''Возвращает словарь соответствия реплик пользователся и ответов бота.'''
    return {
        'привет':'И тебе привет!',
        'как дела': 'лучше всех',
        'пока':'увидимся',
        'пока!': 'Баюшки'
    }

def make_ans(ans_dict, dict_key, defans):
    '''Формирует ответ по словарю, ключу и значению по умолчанию.'''
    return ans_dict.get(dict_key, defans)

def get_ans(user_str, defans='даже не знаю'):
    '''Формирует ответ для пользователя.'''
    user_str = user_str.lower()
    return make_ans(get_bot_dict(), user_str, defans)

def rand_positive(deftext='даже не знаю'):
    '''Генерирует позитивный текст.'''
    positive_list = [
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

    i = random.randrange(0, len(positive_list) + 1)
    if i < len(positive_list):
        return positive_list[i]
    return deftext

def interact_ans():
    '''Простое общение с пользователем через консоль.'''
    user_input = ''
    while True:
        print(rand_positive())
        user_input = input(':')
        print(get_ans(user_input))
        if user_input == 'пока':
            return

if __name__ == '__main__':
    interact_ans()
