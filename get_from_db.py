from pymongo import MongoClient
import mpu
client = MongoClient('127.0.0.1', 27017)
# print(client.list_database_names())
database = client.csv_to_geo
collection = database['write_to_db']
for geo_id in collection.find({}, {'_id': 0}).sort('geo_id', 1):
    print(geo_id)

lat1 = 50.44029
lon1 = 30.55950
max_dist = 50

# for geo_id in connect.find()
# distance = mpu.haversine_distance((lat1, lon1), (geo_lat, geo_lon))
