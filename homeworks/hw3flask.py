'''Домашняя работа после третьего занятия, лекции'''
from flask import Flask, request
import requests

city_id = 524901
apikey = 'cf90636aa494e41b0365ce34aa48722a'


def req_api_json(url):
    '''Запрос api и возврат json или {}'''
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print('error code', result.status_code)
        return {}


app = Flask(__name__)


@app.route('/test/<int:idd>')
def test(idd):
    '''Тест извлечения из адреса по шаблону с определенным типом'''
    return 'test id={}'.format(idd)


@app.route('/temp')
def show_temp():
    '''Скачивание и вывод темпиратуры в Москве'''
    apiurl = 'http://api.openweathermap.org/data/2.5'
    url = '{}/weather?id={}&APPID={}&units=metric'.format(apiurl,city_id,apikey)
    print(url)
    res_json = req_api_json(url)
    print(res_json)
    return str(res_json.get('main',{}).get('temp','недоступно'))


@app.route('/names')
def show_names():
    '''Скачивание и вывод информации об именах'''
    res_json = req_api_json('http://api.data.mos.ru/v1/datasets/2009/rows')

    try:
        r_year = int(request.args.get('year',0))
    except ValueError:
        r_year = 0

    tab_body = ''
    for row in res_json:
        try:
            year = int(row.get('Cells',{}).get('Year',0))
            if r_year and r_year != year:
                continue
            month = row.get('Cells',{}).get('Month','')
            name = row.get('Cells',{}).get('Name','')
            tab_body += '<tr><td>{}</td><td align="right">{}</td><td align="right">{}</td></tr>'.format(name,month,year)
        except ValueError:
            continue

    tab_head = '<tr><th>{}</th><th>{}</th><th>{}</th></tr>'.format('Имя','Месяц','Год')
    names_tab = '<table>{}{}</table>'.format(tab_head,tab_body)
    return names_tab


if __name__ == '__main__':
    app.run()
