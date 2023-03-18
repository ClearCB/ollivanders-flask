from pymongo import MongoClient, errors
from repository.models.initial_inventory import items_day_zero
from json import loads, dumps
import os


class Database:
    def __init__(self, db_uri):

        self.uri = db_uri
        self.client = None
        self.db = None
        self.collection = None

    def get_uri(self):

        return self.uri

    def get_db(self):

        return self.db

    def set_collection(self, collection):

        self.collection = self.get_db()[collection]

    def get_collection(self):

        return self.collection

    def connect(self):

        try:

            self.client = MongoClient(self.get_uri(), serverSelectionTimeoutMS=1000)
            self.client.server_info()

        except errors.ConnectionFailure:

            self.client = None
            return (
                "The connection was not posible, please. Check the data and try again"
            )

        else:

            self.db = self.client["ollivander_shop"]
            return "The connection was succesfull!"

    @staticmethod
    def correct_item(item):

        if isinstance(item, dict):

            try:

                loads(dumps(item))
                return True

            except TypeError:

                return False

        else:

            return False

    def insert_item(self, item):

        if Database.correct_item(item):

            return self.collection.insert_one(item)

    def inventory(self):

        return list(self.collection.find())

    def get_item(self, id):

        return self.collection.find_one({"_id": id})

    def delete_item(self, id):

        return self.collection.delete_one({"_id": id}).deleted_count

    def update_item(self, id, **args):

        correct_keys = ["name","sell_in", "quality", "item_type"]
        # Create an update statement
        update_statemen = {}

        # We get the args statement, in which the key : value pair is -> name="name"
        for arg in args:

            if arg in correct_keys:
                # {name = "name"} is added to the update statement
                update_statemen[arg] = args[arg]


        return self.collection.update_one(
            {"_id": id}, {"$set": update_statemen}
        ).modified_count
    
    @staticmethod
    def init_db():

        client = MongoClient(os.environ["MONGO_ATLAS_URI"])
        db = client["ollivander_shop"]
        db.drop_collection("items")
        collection = db["items"]
        collection.insert_many(items_day_zero)
