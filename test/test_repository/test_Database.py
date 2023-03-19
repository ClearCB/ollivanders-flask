from repository.Database import Database
from repository.models.initial_inventory import items_day_zero
import pytest


@pytest.mark.test_create_one
def test_create_one():

    Database.drop_collection()

    item = {
        "_id": 0,
        "name": "Hat",
        "sell_in": 1,
        "quality": 1,
        "item_type": "Conjured",
    }

    assert Database.create_one(item).inserted_id == 0


@pytest.mark.test_read_one
def test_read_one():

    item = {
        "_id": 0,
        "name": "Hat",
        "sell_in": 1,
        "quality": 1,
        "item_type": "Conjured",
    }

    assert Database.read_one(0) == item


@pytest.mark.test_update_one
def test_update_one():

    item = {
        "_id": 0,
        "name": "Hat",
        "sell_in": 1,
        "quality": 1,
        "item_type": "Conjured",
    }
    
    Database.delete_one(0)
    Database.create_one(item)

    item = {
        "_id": 0,
        "name": "hehe",
        "sell_in": 1,
        "quality": 1,
        "item_type": "Conjured",
    }

    assert Database.update_one(0, {"name": "hehe"}).modified_count == 1

    assert Database.read_one(0) == item


@pytest.mark.test_delete_one
def test_delete_one():

    assert Database.delete_one(0).deleted_count == 1


@pytest.mark.test_inventory
def test_inventory():


    Database.drop_collection()
    Database.init_db()

    assert Database.inventory() == items_day_zero