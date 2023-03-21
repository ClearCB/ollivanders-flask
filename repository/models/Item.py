from domain.items.AgedBrie import AgedBrie
from domain.items.Backstage import Backstage
from domain.items.Sulfuras import Sulfuras
from domain.items.NormalItem import NormalItem
from domain.items.Conjured import Conjured


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

        item_object = eval(
            self.item_type + str(tuple([self.name, self.sell_in, self.quality]))
        )

        item_object.update_quality()

        return {"sell_in": item_object.sell_in, "quality": item_object.quality}
    
    @staticmethod
    def is_correct(item):
            
        correct_item_type = ["Sulfuras","NormalItem","Conjured","Backstage","AgedBrie"]
        correct_keys = ["_id","sell_in", "quality","item_type","name"]
        int_values = ["sell_in","quality"]

        # The json must have 5 values
        if len(item) != 5:
            return False
        
        for key in item:
            
            # Check if keys are correct
            if key not in correct_keys:
                return False
            
            # Check if the values are correct type
            elif key in int_values:
                try:
                    int(item[key])
                except ValueError:
                    return False

            # Check if the item type is correct
            elif key == "item_type" and item[key] not in correct_item_type:

                return False

        return True
