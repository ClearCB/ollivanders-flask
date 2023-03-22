from pymongo import MongoClient
from repository.models.initial_inventory import items_day_zero
import os


class Database:

    @staticmethod
    def connect(database):

        client = MongoClient(os.environ.get("MONGO_ATLAS_URI"))
        return client[database]

    @staticmethod
    def collection(collection):

        return Database.connect("ollivander_shop")[collection]

    @staticmethod
    def init_db():


        Database.collection("items").insert_many(items_day_zero)


    @staticmethod
    def drop_collection():

        client = MongoClient(os.environ.get("MONGO_ATLAS_URI"))
        db = client["ollivander_shop"]
        db.drop_collection("items")

    @staticmethod
    def read_one(id):

        Database.collection("items").find_one({"_id":id})

    @staticmethod
    def delete_one(id):

        Database.collection("items").delete_one({"_id":id})

    @staticmethod
    def create_one(item):

        Database.collection("items").insert_one(item)

    @staticmethod
    def update_one(id, update_statement):

        Database.collection("items").update_one({"_id":id},{"$set":update_statement})


    @staticmethod
    def inventory():

        return list(Database.collection("items").find())