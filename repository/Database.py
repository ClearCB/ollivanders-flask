from pymongo import MongoClient, errors
from repository.models.initial_inventory import items_day_zero
import os


class Database:

    @staticmethod
    def init_db():

        client = MongoClient(os.environ.get("MONGO_ATLAS_URI"))
        db = client["ollivander_shop"]
        collection = db["items"]
        collection.insert_many(items_day_zero)


    @staticmethod
    def drop_collection():

        client = MongoClient(os.environ.get("MONGO_ATLAS_URI"))
        db = client["ollivander_shop"]
        db.drop_collection("items")

    @staticmethod
    def read_one(id):

        client = MongoClient(os.environ.get("MONGO_ATLAS_URI"))
        db = client["ollivander_shop"]
        collection = db["items"]

        return collection.find_one({"_id":id})

    @staticmethod
    def delete_one(id):

        client = MongoClient(os.environ.get("MONGO_ATLAS_URI"))
        db = client["ollivander_shop"]
        collection = db["items"]

        return collection.delete_one({"_id":id})

    @staticmethod
    def create_one(item):

        client = MongoClient(os.environ.get("MONGO_ATLAS_URI"))
        db = client["ollivander_shop"]
        collection = db["items"]

        return collection.insert_one(item)

    @staticmethod
    def update_one(id, update_statement):

        client = MongoClient(os.environ.get("MONGO_ATLAS_URI"))
        db = client["ollivander_shop"]
        collection = db["items"]

        return collection.update_one({"_id":id},{"$set":update_statement})


    @staticmethod
    def inventory():

        client = MongoClient(os.environ.get("MONGO_ATLAS_URI"))
        db = client["ollivander_shop"]
        collection = db["items"]

        return list(collection.find())