from domain.items.AgedBrie import AgedBrie
from domain.items.Backstage import Backstage
from domain.items.Sulfuras import Sulfuras
from domain.items.NormalItem import NormalItem
from domain.items.Conjured import Conjured



class Item:

    # Posible item types
    correct_item_type = ["Sulfuras","NormalItem","Conjured","Backstage","AgedBrie"]
    # Keys that an item MUST have
    correct_keys = ["_id","sell_in", "quality","item_type","name"]
    # Data type that must be int
    int_values = ["sell_in","quality"]

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
    def is_correct_json(item):
            

        # The json must have 5 values
        if len(item) != len(Item.correct_keys):
            return False
        
        for key in item:
            
            # Check if keys are correct
            if key not in Item.correct_keys:
                return False
            
            # Check if the values are correct type
            elif key in Item.int_values:
                try:
                    int(item[key])
                except ValueError:
                    return False

            # Check if the item type is correct
            elif key == "item_type" and item[key] not in Item.correct_item_type:

                return False

        return True
    
    @staticmethod
    def correct_update_statement(update_statement):

        for key in update_statement:
            
            # Check if keys are correct
            if key == "_id" or key == "item_type":
                return False
            
            # Check if the values are correct type
            elif key in Item.int_values:
                try:
                    int(update_statement[key])
                except ValueError:
                    return False

        return True
