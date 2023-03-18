from repository.Database import Database
from repository.models.Item import Item
import os

class Services:

    @staticmethod
    def create_one(id, **args):

        db = Database(os.environ["MONGO_ATLAS_URI"])
        db.connect()
        db.set_collection("inventory")
        item = Item(id, args["name"], args["sell_in"], args["quality"], args["item_type"])

        return db.insert_item(item.to_collection())

    @staticmethod
    def get_one(id):

        db = Database(os.environ["MONGO_ATLAS_URI"])
        db.connect()
        db.set_collection("inventory")

        return db.get_item(id)

    @staticmethod
    def inventory():

        db = Database(os.environ["MONGO_ATLAS_URI"])
        db.connect()
        db.set_collection("inventory")
        return db.inventory()

    @staticmethod
    def delete_one(id):

        db = Database(os.environ["MONGO_ATLAS_URI"])
        db.connect()
        db.set_collection("inventory")
        return db.delete_item(id)
    
    @staticmethod
    def update_one(id, **args):

        db = Database(os.environ["MONGO_ATLAS_URI"])
        db.connect()
        db.set_collection("inventory")

        return db.update_item(id, **args)