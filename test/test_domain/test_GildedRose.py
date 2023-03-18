from domain.GildedRose import GildedRose
from test.test_domain.test_variables import items_day_one, items_day_thirty
import pytest


@pytest.fixture
def shop():
    test_gilded_rose = GildedRose(items_day_one)
    return test_gilded_rose


@pytest.mark.test_update_inventory
def test_update_inventory(shop):
    for i in range(1, 30):
        shop.update_inventory()

    for j in range(0, 9):
        assert shop.items[j].name == items_day_thirty[j].name
        assert shop.items[j].sell_in == items_day_thirty[j].sell_in
        assert shop.items[j].quality == items_day_thirty[j].quality
