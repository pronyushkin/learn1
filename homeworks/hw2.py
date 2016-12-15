'''Домашняя работа после второго занятия'''
from datetime import datetime, date, timedelta
#pip install python-dateutil
from dateutil.relativedelta import relativedelta
import csv

def exercise_datatime():
    '''
    Напечатайте в консоль даты: вчера, сегодня, месяц назад
    Превратите строку "01/01/17 12:10:03.234567" в объект datetime
    '''
    #приведение к дате dt_now = datetime.now().date()
    dt_now = datetime.today()
    print('сегодня', dt_now.strftime('%d.%m.%Y'))
    print('вчера', (dt_now - timedelta(days=1)).strftime('%d.%m.%Y'))
    print('месяц назад', (dt_now - relativedelta(months=1)).strftime('%d.%m.%Y'))

def exercise_filework():
    '''
    Скачайте файл по ссылке
    Прочитайте его и подсчитайте количество слов в тексте
    '''
    content = ''
    with open('referat.txt', 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('\n',' ').replace('  ',' ')
    content_as_list = content.split(' ')
    print('количество слов в файле {}'.format(len(content_as_list)))

def exercise_csv():
    '''
    Возьмите словарь с ответами
    Запишите его содержимое в формате csv в формате: "ключ"; "значение". 
    Каждая пара ключ-значение должна располагаться на отдельной строке
    TODO выходной файл содержит дополнительные переводы строки
    '''
    data = {
        'привет':'И тебе привет!',
        'как дела': 'лучше всех',
        'пока':'увидимся',
        'пока!': 'Баюшки'
    }
    fields = ['ключ', 'значение']
    csv_data = []
    while data:
        rec = data.popitem()
        row = { fields[0]:rec[0],fields[1]:rec[1]}
        csv_data.append(row)

    print(csv_data)
    with open('export.csv', 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for row in csv_data:
            writer.writerow(row)

if __name__ == '__main__':
    #exercise_datatime()
    #exercise_filework()
    exercise_csv()
