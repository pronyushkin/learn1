'''Подсчет слов.'''

def word_counter(msg_text):
    '''Считаем количество слов.'''
    print('word_counter', msg_text)
    begin_index = msg_text.find('"')
    if begin_index == -1:
        return 'Надо было ввести слова в кавычках'

    end_index = msg_text.rfind('"')
    if begin_index == end_index or begin_index + 1 == end_index:
        return 'Надо было ввести слова в кавычках'

    user_words = msg_text[begin_index + 1:end_index].strip()
    splited = user_words.split(' ')
    w_count = 0
    for i in splited:
        if i != ' ' and i != '':
            w_count += 1
    if not w_count:
        return 'в кавычках должны были быть слова'
    return 'Количество введенных слов {}'.format(w_count)

if __name__ == '__main__':
    print(word_counter(input('введите фразу: ')))