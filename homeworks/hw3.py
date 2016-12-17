'''Домашняя работа после третьего занятия'''
import csv
import json


def exercise_csv_bus_station():
    '''
    Считать из csv-файла (с http://data.mos.ru/datasets/752) 
    количество остановок, вывести улицу, на которой больше всего остановок.
    '''
    with open('data-398-2016-11-07.csv', 'r', encoding='utf-8') as f:
        fields = [  'system_object_id',
                    'global_id',
                    'Name',
                    'Longitude_WGS84',
                    'Latitude_WGS84',
                    'Street',
                    'AdmArea',
                    'District',
                    'RouteNumbers',
                    'OperatingOrgName',
                    'EntryState',
                    'Pavilion',
                    'Direction',
                    'ID',
                    'StationName',
                    'geoData'
                ]
        reader = csv.DictReader(f, fields, delimiter=';')
        counter = {}
        max = ('none', 0)
        for row in reader:
            #print(type(row))
            #print('row data\n',row)
            street = row.get('Street',False)
            if street:
                counter.setdefault(street, 0)
                counter[street] += 1
                if max[1] < counter[street]:
                    max = (street,counter[street])
        print(max)


def exercise_json_metro_station():
    '''
    В этом задании требуется определить, на каких станциях московского метро сейчас идёт ремонт эскалаторов и вывести на экран их названия.
    '''
    with open('data-397-2016-11-24.json', 'r', encoding='utf-8') as f:
        js_content = json.load(f, encoding='utf-8')
        print(type(js_content))
        repair_station = []
        for row in js_content:
            repair = row.get('RepairOfEscalators',False)
            if repair:
                if len(repair):
                    station_name = row.get('Name','имя не определено, ')
                    station_name = station_name.split(',')[0]
                    repair_station.append(station_name)
    repair_station_set = set(repair_station)
    print(repair_station_set)


if __name__ == '__main__':
    #exercise_csv_bus_station()
    exercise_json_metro_station()
