from repository.models import Item
import pytest


@pytest.fixture
def test_model_item():

    item = Item(1,"Aged Brie", 19,23)
    return item

@pytest.mark.test_constructor
def test_constructor(test_model_item):

    assert test_model_item != None

@pytest.mark.test_to_collection
def test_to_collection(test_model_item):

    sample_item_json = {
        "_id":1,
        "name":"Aged Brie",
        "sell_in":19,
        "quality":23
    }

    assert test_model_item.to_collection() == sample_item_json