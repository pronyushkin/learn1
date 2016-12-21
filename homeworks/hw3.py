'''Домашняя работа после третьего занятия'''
import csv
import json


def exercise_csv_bus_station(filename):
    '''
    Считать из csv-файла (с http://data.mos.ru/datasets/752) 
    количество остановок, вывести улицу, на которой больше всего остановок.
    '''
    with open(filename, 'r', encoding='utf-8') as f:
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


def exercise_json_metro_station(filename):
    '''
    В этом задании требуется определить, на каких станциях московского метро сейчас идёт ремонт эскалаторов и вывести на экран их названия.
    '''
    with open(filename, 'r', encoding='utf-8') as f:
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


def exercise_bus_near_metro(bus_file,metro_file):
    '''
    Объединить наборы данных из предыдущих задач и посчитать, у какой станции метро больше всего остановок (в радиусе 0.5 км)
    '''
    bus_stations = []
    with open(bus_file, 'r', encoding='utf-8') as f:
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
        need_skip = True
        for row in reader:
            if need_skip:
                need_skip = False
                continue
            bus_stations.append((float(row['Longitude_WGS84']), float(row['Latitude_WGS84'])))
            
    metro_stations = {}
    with open(metro_file, 'r', encoding='utf-8') as f:
        js_content = json.load(f, encoding='utf-8')
        
        for row in js_content:
            station_name = row.get('Name','имя не определено, ')
            station_name = station_name.split(',')[0]
            if station_name not in metro_stations:
                metro_stations[station_name] = [(float(row['Longitude_WGS84']), float(row['Latitude_WGS84']))]
            else:
                metro_stations[station_name].append((float(row['Longitude_WGS84']), float(row['Latitude_WGS84'])))
    #print(bus_stations)
    #print(metro_stations)
    max = ('none', 0)
    while metro_stations:
        station = metro_stations.popitem()
        print(station)
        for bus_coord in bus_stations:
            print('b1',bus_coord)
            for coord in station[1]:
                print('c1',coord)
        break


if __name__ == '__main__':
    #exercise_csv_bus_station('data-398-2016-11-07.csv')
    #exercise_json_metro_station('data-397-2016-11-24.json')
    exercise_bus_near_metro('data-398-2016-11-07.csv', 'data-397-2016-11-24.json')
