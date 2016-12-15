'''заметки по поводу списков'''


#списки
CONST_LIST_A = [3, 4, 1, 5]
#Добавление в конец
CONST_LIST_A.append(99)
CONST_LIST_B = [7, 4, 3, 2]
#сложение работает как для строк, т.е. второй добавится в конец
print(CONST_LIST_A + CONST_LIST_B)
#Итерации по списку
for s in CONST_LIST_B:
    print(s)

#разворот списка reversed возвращает упрощенный объект, его надо превратить обратно в список
print(list(reversed(CONST_LIST_B)))
#сортировка возвращает нормальный список
print(sorted(CONST_LIST_B))

#доступ по индексу
print(CONST_LIST_B[0])
print(CONST_LIST_B[len(CONST_LIST_B)-1])
#доступ по диапазону (полуоткрыт)
print(CONST_LIST_B[1:3])
#доступ с конца
print(CONST_LIST_B[-1])

#словари
I_DONT_KNOW_WHY_IT_IS_CONST = {'key1': 5, 'key2': 'вас'}

I_DONT_KNOW_WHY_IT_IS_CONST['newkey'] = 'new value'
#безопасный доступ
I_DONT_KNOW_WHY_IT_IS_CONST.get('akey', 'have no item')


#проверить наличие ключа в словаре
print('key' in I_DONT_KNOW_WHY_IT_IS_CONST) # вернет True если в словаре
print('key' not in I_DONT_KNOW_WHY_IT_IS_CONST) # вернет False если в словаре

for key, value in I_DONT_KNOW_WHY_IT_IS_CONST.items():
    print('key={} value={}'.format(key, value))

for key in I_DONT_KNOW_WHY_IT_IS_CONST:
    print(key)

try:
    del I_DONT_KNOW_WHY_IT_IS_CONST['key1']
except KeyError:
    print('error')
