from domain.items.AgedBrie import AgedBrie
from domain.items.NormalItem import NormalItem
from domain.items.Sulfuras import Sulfuras
from domain.items.Conjured import Conjured
from domain.items.Backstage import Backstage
from domain.items.item_names import names 

class Item:
    def __init__(self, id, name, sell_in, quality, item_type):
        self.id = id
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.item_type = item_type

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_sell_in(self):
        return self.sell_in

    def get_quality(self):
        return self.quality

    def get_item_type(self):
        return self.item_type

    def to_collection(self):
        # Convert to json the object that is in correct format to create a new document in mongoDB.
        return {
            "_id": self.get_id(),
            "name": self.get_name(),
            "sell_in": self.get_sell_in(),
            "quality": self.get_quality(),
            "item_type": self.get_item_type()
        }

    @staticmethod
    def to_object(name, sell_in, quality, item_type):

        # Using globals that allow us to acces to all the variables.
        item_object = globals()[item_type](name, int(sell_in), int(quality))

        return item_object
        