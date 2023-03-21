from repository.models.Item import Item

dextitry = "+5 Dexterity Vest"
agedBrie = "Aged Brie"
elixir = "Elixir of the Mongoose"
sulfuras = "Sulfuras, Hand of Ragnaros"
backstage = "Backstage passes to a TAFKAL80ETC concert"
conjured = "Conjured Mana Cake"

items_day_zero = [
    Item(0, "test_item", 5, 10, "NormalItem").to_collection(),
    Item(1, dextitry, 10, 20, "Conjured").to_collection(),
    Item(2, agedBrie, 2, 0, "AgedBrie").to_collection(),
    Item(3, elixir, 5, 7, "NormalItem").to_collection(),
    Item(4, sulfuras, 0, 80, "Sulfuras").to_collection(),
    Item(5, sulfuras, -1, 80, "Sulfuras").to_collection(),
    Item(6, backstage, 15, 20, "Backstage").to_collection(),
    Item(7, backstage, 10, 49, "Backstage").to_collection(),
    Item(8, backstage, 5, 49, "Backstage").to_collection(),
    Item(9, conjured, 3, 6, "Conjured").to_collection(),
]
