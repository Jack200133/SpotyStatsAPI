import pymongo
import json


client = pymongo.MongoClient("mongodb+srv://jackal:jackal@spotifystats.1emngx6.mongodb.net/?retryWrites=true&w=majority")
db = client['SpotyStats']

collection = db['canciones']

with open("./src/archivos/canciones_final.json", "r",encoding='Utf-8') as j:
    data = json.load(j)

collection.insert_many(data)

collection = db['reproducciones']

with open("./src/archivos/reproducciones_final.json", "r",encoding='Utf-8') as j:
    data2 = json.load(j)

collection.insert_many(data2)