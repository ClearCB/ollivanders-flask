from repository.models.check_item import is_correct_json, correct_update_statement
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
    sample_item_json = {
        "_id": 1,
        "name": aged_brie_n,
        "sell_in": 19,
        "quality": 23,
        "item_type": "AgedBrie",
    }

    assert test_model_item.to_collection() == sample_item_json

@pytest.mark.test_update_statement
def test_update_statement(test_model_item):

    assert test_model_item.update_statement() == {"sell_in":18,"quality":24}

@pytest.mark.test_correct_json
def test_correct_json():

    assert is_correct_json({"_id":2}) == False
    assert is_correct_json({"_id":2,"name":"Sulfuras"}) == False
    assert is_correct_json({"_id":2, "name":"Sulfuras","s":"Sulfuras","r":"Sulfuras","h":"Sulfuras"}) == False
    assert is_correct_json({"_id":2, "name":"Sulfuras","sell_in":"Sulfuras","quality":"Sulfuras","item_type":"Sulfuras"}) == False
    assert is_correct_json({"_id":2, "name":"Sulfuras","sell_in":2,"quality":3,"item_type":"Sulfuras"}) == True
    assert is_correct_json({"_id":2, "name":"Sulfuras","sell_in":2,"quality":3,"item_type":"as"}) == False

pytest.mark.test_correct_update_statement
def test_correct_update_statement():

    assert correct_update_statement({"_id":2,"name":"Sulfuras"}) == False
    assert correct_update_statement({"_id":2,"sell_in":2}) == False
    assert correct_update_statement({"name":"Sulfuras","sell_in":2}) == True
    assert correct_update_statement({"name":"Sulfuras","sell_in":2}) == True
    assert correct_update_statement({"name":"Sulfuras","sell_in":2,"quality":"as"}) == False
    assert correct_update_statement({"name":"Sulfuras","sell_in":2,"quality":5}) == True
