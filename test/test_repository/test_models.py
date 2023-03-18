from repository.models.Item import Item
from domain.items.AgedBrie import AgedBrie
import pytest

aged_brie_n = "Aged Brie"

# Item test
@pytest.fixture
def test_model_item():
    item = Item(1, aged_brie_n, 19, 23, "AgedBrie")
    return item


@pytest.mark.test_constructor
def test_constructor(test_model_item):
    assert test_model_item != None


@pytest.mark.test_to_collection
def test_to_collection(test_model_item):
    sample_item_json = {"_id": 1, "name": aged_brie_n, "sell_in": 19, "quality": 23, "item_type": "AgedBrie"}

    assert test_model_item.to_collection() == sample_item_json

@pytest.mark.test_to_object
def test_to_object():

    aged_brie = AgedBrie(aged_brie_n,1,1)
    aged_brie_ob = Item.to_object(aged_brie_n, 1, "1", "AgedBrie")

    assert isinstance(aged_brie,AgedBrie)
    assert isinstance(aged_brie_ob,AgedBrie)

    assert aged_brie_ob.name == aged_brie.name
    assert aged_brie_ob.sell_in == aged_brie.sell_in
    assert aged_brie_ob.quality == aged_brie.quality