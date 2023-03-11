"""
This class will be the main one, which will be the shop it self.
"""


class GildedRose:
    def __init__(self, items):

        self.items = items

    def update_inventory(self):

        for item in self.items:

            item.update_quality()
