from domain.items.NormalItem import NormalItem
from domain.items.NormalItem import Item

"""
This class will create objects of Backstage type
"""


class Backstage(NormalItem):
    def __init__(self, name, sell_in, quality):

        Item.__init__(self, name, sell_in, quality)

    # Override the method updateQuality
    def updateQuality(self):

        if 5 < self.sell_in <= 10:

            self.setQuality(+2)

        elif 0 < self.sell_in <= 5:

            self.setQuality(+3)

        elif self.sell_in <= 0:

            self.quality = 0

        self.setSellIn()
