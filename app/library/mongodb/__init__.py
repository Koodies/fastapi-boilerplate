from pymongo import MongoClient

db = None


def get_db():
    client = MongoClient("mongodb://localhost:27017/")
    return client["test"]


def insert_one(collection_name, data):
    db = get_db()
    result = db[collection_name].insert_one(data)
    return result.inserted_id
