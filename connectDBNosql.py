from pymongo import MongoClient

def connectDBinsert(json_output):
    client = MongoClient(host="localhost", port=27017)
    db = client.PIDataBase
    data = db.tweets
    data.insert_one(json_output)
