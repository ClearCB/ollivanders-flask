from domain.items.NormalItem import NormalItem
from domain.items.AgedBrie import AgedBrie
from domain.items.Backstage import Backstage
from domain.items.Conjured import Conjured
from domain.items.Sulfuras import Sulfuras
'''
At this file I will store all the variables needed to check if the software
complete each routines correctly, creating an array of objects.
'''

dextitry = "+5 Dexterity Vest"
agedBrie = "Aged Brie"
elixir = "Elixir of the Mongoose"
sulfuras = "Sulfuras, Hand of Ragnaros"
backstage = "Backstage passes to a TAFKAL80ETC concert"
conjured = "Conjured Mana Cake"

items_day_zero = [NormalItem(dextitry, 10, 20),
                AgedBrie(agedBrie, 2, 0),
                NormalItem(elixir, 5, 7),
                Sulfuras(sulfuras, 0, 80),
                Sulfuras(sulfuras, -1, 80),
                Backstage(backstage, 15, 20),
                Backstage(backstage, 10, 49),
                Backstage(backstage, 5, 49),
                Conjured(conjured, 3, 6)
                ]

items_day_one = [NormalItem(dextitry, 9, 18),
                AgedBrie(agedBrie, 1, 1),
                NormalItem(elixir, 4, 6),
                Sulfuras(sulfuras, 0, 80),
                Sulfuras(sulfuras, -1, 80),
                Backstage(backstage, 14, 21),
                Backstage(backstage, 9, 50),
                Backstage(backstage, 4, 50),
                Conjured(conjured, 2, 4)
                ]

items_day_nine = [NormalItem(dextitry, 1, 2),
                AgedBrie(agedBrie, -7, 16),
                NormalItem(elixir, -4, 0),
                Sulfuras(sulfuras, 0, 80),
                Sulfuras(sulfuras, -1, 80),
                Backstage(backstage, 6, 33),
                Backstage(backstage, 1, 50),
                Backstage(backstage, -4, 0),
                Conjured(conjured, -6, 0)
                ]

items_day_nineteen = [NormalItem(dextitry, -9, 0),
                AgedBrie(agedBrie, -17, 36),
                NormalItem(elixir, -14, 0),
                Sulfuras(sulfuras, 0, 80),
                Sulfuras(sulfuras, -1, 80),
                Backstage(backstage, -4, 0),
                Backstage(backstage, -9, 0),
                Backstage(backstage, -14, 0),
                Conjured(conjured, -16, 0)
                ]

items_day_thirty = [NormalItem(dextitry, -20, 0),
                AgedBrie(agedBrie, -28, 50),
                NormalItem(elixir, -25, 0),
                Sulfuras(sulfuras, 0, 80),
                Sulfuras(sulfuras, -1, 80),
                Backstage(backstage, -15, 0),
                Backstage(backstage, -20, 0),
                Backstage(backstage, -25, 0),
                Conjured(conjured, -27, 0)
                ]