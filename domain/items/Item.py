"""
This class will be the one that the other items will adquire.

It will have the atributes about the item (Name, sell-in, quality).
"""


class Item:

    # Constructor
    def __init__(self, name, sell_in, quality):

        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    # Changing the built-in method to call this object in case of needed.
    def __repr__(self):

        return f"{self.name} {self.sell_in} {self.quality}"
