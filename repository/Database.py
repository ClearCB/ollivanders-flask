from pymongo import MongoClient, errors
from repository.models.initial_inventory import items_day_zero
from json import loads, dumps
import os


class Database:

    @staticmethod
    def read_one(id):

        client = MongoClient(os.environ.get("MONGO_ATLAS_URI"))
        db = client["ollivander_shop"]
        collection = db["items"]

        collection.find_one({"_id":id})

    @staticmethod
    def delete_one(id):

        client = MongoClient(os.environ.get("MONGO_ATLAS_URI"))
        db = client["ollivander_shop"]
        collection = db["items"]

        collection.delete_one({"_id":id})

    @staticmethod
    def insert_one(item):

        client = MongoClient(os.environ.get("MONGO_ATLAS_URI"))
        db = client["ollivander_shop"]
        collection = db["items"]

        collection.insert_one(item)

    @staticmethod
    def read_one(id, update_statement):

        client = MongoClient(os.environ.get("MONGO_ATLAS_URI"))
        db = client["ollivander_shop"]
        collection = db["items"]

        collection.update_one({"_id":id},{"$set":{update_statement}})

