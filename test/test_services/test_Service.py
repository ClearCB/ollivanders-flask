from services.Services import Services
from repository.models.Item import Item
from repository.Database import Database
from repository.models.initial_inventory import items_day_zero
import pytest


@pytest.mark.test_create_one
def test_create_one():
    item = Item(0, name="Sulfutas", sell_in=1, quality=1, item_type="Sulfuras")
    Services.delete_one(0)
    assert Services.create_one(item.to_collection()).inserted_id == 0
    Services.delete_one(0)


@pytest.mark.test_get_one
def test_get_one():

    item = Item(0, name="Sulfutas", sell_in=1, quality=1, item_type="Sulfuras")
    Services.delete_one(0)
    assert Services.create_one(item.to_collection()).inserted_id == 0

    assert Services.read_one(0) == item.to_collection()


@pytest.mark.test_get_inventory
def test_get_inventory():

    Database.drop_collection()
    Database.init_db()
    
    assert Services.inventory() == items_day_zero


@pytest.mark.test_update_one
def test_update_one():

    item = {
        "_id": 0,
        "name": "Hat",
        "sell_in": 1,
        "quality": 1,
        "item_type": "Conjured",
    }
    
    Services.delete_one(0)
    Services.create_one(item)

    item = {
        "_id": 0,
        "name": "hehe",
        "sell_in": 1,
        "quality": 1,
        "item_type": "Conjured",
    }

    assert Services.update_one(0, {"name": "hehe"}).modified_count == 1

    assert Services.read_one(0) == item


@pytest.mark.test_delete_one
def test_delete_one():

    assert Services.delete_one(0).deleted_count == 1