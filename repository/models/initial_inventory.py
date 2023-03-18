from repository.models.Item import Item

dextitry = "+5 Dexterity Vest"
agedBrie = "Aged Brie"
elixir = "Elixir of the Mongoose"
sulfuras = "Sulfuras, Hand of Ragnaros"
backstage = "Backstage passes to a TAFKAL80ETC concert"
conjured = "Conjured Mana Cake"

items_day_zero = [
    Item(1,dextitry, 10, 20,"Conjured"),
    Item(2,agedBrie, 2, 0,"AgedBrie"),
    Item(3,elixir, 5, 7,"NormalItem"),
    Item(4,sulfuras, 0, 80,"Sulfuras"),
    Item(5,sulfuras, -1, 80,"Sulfuras"),
    Item(6,backstage, 15, 20,"Backstage"),
    Item(7,backstage, 10, 49,"Backstage"),
    Item(8,backstage, 5, 49,"Backstage"),
    Item(9,conjured, 3, 6,"Conjured")
]