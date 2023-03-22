from repository.Database import Database
from repository.models.Item import Item

error_message = "Please, check the data and try again"


class Services:
    @staticmethod
    def read_one(id):
        return Database.read_one(int(id))

    @staticmethod
    def delete_one(id):
        return Database.delete_one(int(id))

    @staticmethod
    def create_one(item):
        return Database.create_one(item)

    @staticmethod
    def update_one(id, update_statement):
        return Database.update_one(int(id), update_statement)

    @staticmethod
    def inventory():
        return Database.inventory()
