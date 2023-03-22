from domain.items.AgedBrie import AgedBrie
from domain.items.Backstage import Backstage
from domain.items.Sulfuras import Sulfuras
from domain.items.NormalItem import NormalItem
from domain.items.Conjured import Conjured


# In case that we need to add a new class we just need to import it here.
class Item:
    def __init__(self, id, name, sell_in, quality, item_type):
        self.id = id
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.item_type = item_type

    def to_collection(self):
        # Convert to json the object that is in correct format to create a new document in mongoDB.
        return {
            "_id": self.id,
            "name": self.name,
            "sell_in": self.sell_in,
            "quality": self.quality,
            "item_type": self.item_type,
        }

    def update_statement(self):
        # Create an instance of the correct class
        item_object = eval(
            self.item_type + str(tuple([self.name, self.sell_in, self.quality]))
        )
        # Update its quality
        item_object.update_quality()

        # Return the update statement necesary to its category
        return {"sell_in": item_object.sell_in, "quality": item_object.quality}
