from domain.items.NormalItem import Item

"""
This class will adquire the propierties about the Item class, which give it the atributes
and the interface class, that making a comparation with java, we will need a constraint 
to keep our software under the desing per contract => We need updateables items to continue.
"""


class NormalItem(Item):

    # Constructor
    def __init__(self, name, sell_in, quality):

        Item.__init__(self, name, sell_in, quality)

    # Getters/Setters
    def getName(self):

        return self.name

    def getSellIn(self):

        return self.sell_in

    def getQuality(self):

        return self.quality

    def setName(self, new_name):

        self.name = new_name

    def setSellIn(self):

        self.sell_in = self.sell_in + -1

    # By domain, the quality has the following behaviour (check ProblemSpecificationRequirements.txt)
    def setQuality(self, quality_increment):

        self.quality += quality_increment

        if self.quality > 50:

            self.quality = 50

        elif self.quality < 0:

            self.quality = 0

        assert (
            0 <= self.quality <= 50
        )  # Invariant, the quality must be always under those values

    # Override the method updateQuality adapted to NormalItems
    def updateQuality(self):

        if self.sell_in >= 0:

            self.setQuality(-1)

        elif self.sell_in < 0:

            self.setQuality(-2)

        # We change the value of sell-in after updating quality
        self.setSellIn()
