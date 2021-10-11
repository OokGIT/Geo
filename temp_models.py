from mongoengine import *
connect(host="mongodb://127.0.0.1:27017/csv_to_geo")


class WriteToDb(Document):
    oblast = StringField()
    rayon = StringField()
    geo_id = StringField()
    geo_lon = DecimalField()
    geo_lat = DecimalField()

