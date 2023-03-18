from domain.items.NormalItem import NormalItem

"""
This class will be for Sulfuras, legendary item.
"""


class Sulfuras(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    # Override new updateQuality method
    def update_quality(self):
        self.quality = 80
