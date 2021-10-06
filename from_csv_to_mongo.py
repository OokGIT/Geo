import csv
import mpu
from _models import WriteToDb

lat1 = 50.44029
lon1 = 30.55950

rows = []
file = open('ua-list.csv', 'r', encoding='windows-1251')
csv_reader = list(csv.reader(file, delimiter=';'))
for elem in csv_reader:
    # print(row)
    # rows.append(elem)
    distance = mpu.haversine_distance((lat1, lon1), (elem[4], elem[3]))
    print(distance)
    # WriteToDb(oblast=elem[0], rayon=elem[1], geo_id=elem[2],
    #           geo_lon=elem[3], geo_lat=elem[4]).save()
    # print(row[0])
file.close()
    # for elem in rows:
    #     WriteToDb(oblast=elem[0], rayon=elem[1], geo_id=elem[2],
    #               geo_lon=elem[3], geo_lat=elem[4]).save()
        # # oblast = elem[0]
        # # rayon = elem[1]
        # geo_id = elem[2]
        # geo_lon = float(elem[3])
        # geo_lat = float(elem[4])
        # print(geo_id, float(geo_lat), float(geo_long))
        # distance = mpu.haversine_distance((lat1, lon1), (geo_lat, geo_lon))
        # if geo_id == 'РАХІВ':
        #     print(distance)
