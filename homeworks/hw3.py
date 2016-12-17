'''Домашняя работа после третьего занятия'''
import csv

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


if __name__ == '__main__':
    exercise_csv_bus_station()
