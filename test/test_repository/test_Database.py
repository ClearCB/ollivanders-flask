from repository.Database import Database
import pytest


@pytest.mark.test_create_one
def test_create_one():

    item = {
        "_id":001,
        "name":"Hat",
        "sell_in":1,
        "quality":1,
        "item_type":"Conjured"
    }

    assert Database.create_one(item).inserted_id==1

@pytest.mark.test_read_one
def test_read_one():

    item = {
        "_id":001,
        "name":"Hat",
        "sell_in":1,
        "quality":1,
        "item_type":"Conjured"
    }

    assert Database.read_one(001)==item

@pytest.mark.test_delete_one
def test_delete_one():

    assert Database.delete_one(001).deleted_count==1

@pytest.mark.test_update_one
def test_update_one():

    item = {
        "_id":001,
        "name":"Hat",
        "sell_in":1,
        "quality":1,
        "item_type":"Conjured"
    }

    assert Database.update_one(001, {"name":"hehe"}).modified_count == 1

    assert Database.find_one(001) == item