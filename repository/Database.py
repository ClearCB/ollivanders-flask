from pymongo import MongoClient, errors
from json import loads, dumps


class Database:
    def __init__(self, db_uri):

        self.uri = db_uri
        self.client = None
        self.db = None

    def get_uri(self):

        return self.uri

    def get_db(self):

        return self.db

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

            return self.db["inventory"].insert_one(item)

    def inventory(self):

        return list(self.db["inventory"].find())