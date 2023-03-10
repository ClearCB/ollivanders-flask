from domain.items.NormalItem import NormalItem
from domain.items.NormalItem import Item

"""
Class for the new category conjured
"""


class Conjured(NormalItem):

    # Constructor
    def __init__(self, name, sell_in, quality):

        Item.__init__(self, name, sell_in, quality)

    # Override the method updateQuality
    def updateQuality(self):

        if self.sell_in >= 0:

            self.setQuality(-2)

        elif self.sell_in < 0:

            self.setQuality(-4)

        self.setSellIn()
