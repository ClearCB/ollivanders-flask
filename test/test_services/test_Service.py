
import pytest

@pytest.mark.test_create_one
def test_create_one():

    assert Services.create_one(1,"Sulfutas",1,1,"Sulfuras").inserted_id == 1

@pytest.mark.test_get_one
def test_get_one():

    item = {
        "_id":1,
        "name":"Sulfutas",
        "sell_in":1,
        "quality":1,
        "item_type":"Sulfuras"
        }

    assert Services.get_one(1) == item

@pytest.mark.test_get_inventory
def test_get_inventory():

    Services.create_one(2,"Sulfutas",1,1,"Sulfuras")

    inventory = [
        Services.get_one(1),
        Services.get_one(2)
        ]
    
    assert Services.inventory() == inventory


@pytest.mark.test_update_one
def test_update_one():

    assert Services.update_one(1,name="haha").modified_count == 1

    item = {
        "_id":1,
        "name":"haha",
        "sell_in":1,
        "quality":1,
        "item_type":"Sulfuras"
        }
    
    assert Services.get_one(1) == item

@pytest.mark.test_delete_one
def test_delete_one():

    assert Services.create_one(1,"Sulfutas",1,1,"Sulfuras").inserted_id == 1