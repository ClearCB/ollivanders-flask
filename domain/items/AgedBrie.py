from domain.items.NormalItem import NormalItem

"""
We will create a class called 'Aged brie', in which we will inheritance the class
NormalItem but overriding the method updateQuality adapting it to each product
"""


class AgedBrie(NormalItem):

    # Constructor, inheritated from Item class.
    def __init__(self, name, sell_in, quality):

        NormalItem.__init__(self, name, sell_in, quality)

    # Override the method updateQuality
    def update_quality(self):

        if self.sell_in > 0:
            self.set_quality(+1)

        else:
            self.set_quality(+2)

        self.set_sell_in()
