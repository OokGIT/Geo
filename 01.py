import csv
import mpu

lat1 = 50.44029
lon1 = 30.55950
min_geo_range = 20
max_geo_range = 50

rows = {}
file = open('ua-list.csv', 'r', encoding='windows-1251')
csv_reader = list(csv.reader(file, delimiter=';'))
for elem in csv_reader:
    distance = mpu.haversine_distance((lat1, lon1),
                                      (float(elem[4]), float(elem[3])))
    rows[elem[2]] = distance
file.close()
sorted_rows = dict(sorted(rows.items(), key=lambda x: x[1]))
for k, v in sorted_rows.items():
    if min_geo_range <= v <= max_geo_range:
        print(k, round(v, 1))
