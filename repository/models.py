class Item:
    def __init__(self, id, name, sell_in, quality):
        self.id = id
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_sell_in(self):
        return self.sell_in

    def get_quality(self):
        return self.quality

    def to_collection(self):
        # Convert to json the object that is in correct format to create a new document in mongoDB.
        return {
            "_id": self.get_id(),
            "name": self.get_name(),
            "sell_in": self.get_sell_in(),
            "quality": self.get_quality(),
        }
