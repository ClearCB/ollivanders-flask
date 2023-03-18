from domain.items.NormalItem import NormalItem

"""
Class for the new category conjured
"""


class Conjured(NormalItem):
    # Constructor
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    # Override the method updateQuality
    def update_quality(self):
        if self.sell_in >= 0:
            self.set_quality(-2)

        elif self.sell_in < 0:
            self.set_quality(-4)

        self.set_sell_in()
