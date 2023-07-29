import os
from pymongo import MongoClient
from pymongo.collection import Collection
from typing import Optional


class Database:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.client = MongoClient(os.getenv("MONGO_CONNECTION_URI", None))
            cls.instance.db = cls.instance.client["test"]
        return cls.instance

    def collection(self, collection_name) -> Collection:
        return self.instance.db[collection_name]


def get_db() -> Optional[Database]:
    return Database()
