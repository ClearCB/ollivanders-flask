from domain.items.NormalItem import NormalItem

"""
This class will create objects of Backstage type
"""


class Backstage(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    # Override the method updateQuality
    def update_quality(self):
        if self.sell_in > 10:
            self.set_quality(+1)

        elif 5 < self.sell_in <= 10:
            self.set_quality(+2)

        elif 0 < self.sell_in <= 5:
            self.set_quality(+3)

        elif self.sell_in <= 0:
            self.quality = 0

        self.set_sell_in()
