
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
