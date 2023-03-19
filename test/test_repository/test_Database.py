from repository.Database import Database
from repository.models.initial_inventory import items_day_zero
from pymongo import MongoClient
import os
import pytest

aged_brie = "Aged Brie"


# Creating an aditional collection / database to the test.
@pytest.fixture
def test_db_correct():
    test_ollivanders_database_correct = Database(os.environ["MONGO_ATLAS_URI"])
    test_ollivanders_database_correct.connect()
    test_ollivanders_database_correct.set_collection("test_inventory")
    return test_ollivanders_database_correct


@pytest.fixture
def test_db_not_correct():
    test_ollivanders_database_incorrect = Database("hellothisisnotgoingtowork")
    test_ollivanders_database_incorrect.connect()
    return test_ollivanders_database_incorrect


@pytest.fixture
def test_item_one():
    item = {
        "_id": 1,
        "name": aged_brie,
        "sell_in": 10,
        "quality": 30,
        "item_type": aged_brie,
    }
    return item


@pytest.fixture
def test_item_two():
    item = {
        "_id": 2,
        "name": aged_brie,
        "sell_in": 10,
        "quality": 30,
        "item_type": aged_brie,
    }
    return item


@pytest.mark.test_constructor
def test_constructor(test_db_correct, test_db_not_correct):
    assert test_db_correct != None
    assert test_db_not_correct != None


@pytest.mark.test_db_connection
def test_db_connection():
    test_correct = Database(os.environ["MONGO_ATLAS_URI"])

    test_not_correct = Database("<xvzdhsdfhasf2334")

    assert test_correct.connect() == "The connection was succesfull!"
    assert (
        test_not_correct.connect()
        == "The connection was not posible, please. Check the data and try again"
    )


@pytest.mark.test_set_working_collection
def test_set_working_collection(test_db_correct):
    test_db_correct.set_collection("inventory")
    assert test_db_correct.get_collection() == test_db_correct.get_db()["inventory"]
    test_db_correct.set_collection("test_inventory")
    assert (
        test_db_correct.get_collection() == test_db_correct.get_db()["test_inventory"]
    )


@pytest.mark.test_get_client
def test_get_client(test_db_correct, test_db_not_correct):
    assert isinstance(test_db_correct.client, MongoClient)
    assert test_db_not_correct.client == None


@pytest.mark.test_get_database
def test_get_databaase(test_db_correct):
    assert test_db_correct.get_db() == test_db_correct.client["ollivander_shop"]


@pytest.mark.test_correct_item
def test_correct_item(test_item_one, test_item_two):
    item = {"_id": 2, "name": aged_brie, "sell_in": Database("s"), "quality": 30}

    assert Database.correct_item(test_item_one)
    assert Database.correct_item(test_item_two)
    assert Database.correct_item(item) == False
    assert Database.correct_item(["AHHS"]) == False
    assert Database.correct_item(1) == False


@pytest.mark.test_insert_item
def test_insert_item(test_db_correct, test_item_one, test_item_two):
    test_db_correct.get_db().drop_collection("test_inventory")

    assert test_db_correct.insert_item(test_item_one).inserted_id == 1
    assert test_db_correct.insert_item(test_item_two).inserted_id == 2


@pytest.mark.test_get_inventory
def test_get_inventory(test_db_correct):
    inventory_test = [
        {
            "_id": 1,
            "name": aged_brie,
            "sell_in": 10,
            "quality": 30,
            "item_type": aged_brie,
        },
        {
            "_id": 2,
            "name": aged_brie,
            "sell_in": 10,
            "quality": 30,
            "item_type": aged_brie,
        },
    ]

    assert test_db_correct.inventory() == inventory_test


@pytest.mark.test_get_item
def test_get_item(test_db_correct):
    assert test_db_correct.get_item(1) == {
        "_id": 1,
        "name": aged_brie,
        "sell_in": 10,
        "quality": 30,
        "item_type": aged_brie,
    }


@pytest.mark.test_delete_item
def test_delete_item(test_db_correct):
    assert test_db_correct.delete_item(1) == 1
    assert test_db_correct.delete_item(2) == 1
    assert test_db_correct.delete_item(3) == 0


@pytest.mark.test_update_item
def test_update_item(test_db_correct, test_item_one):
    test_db_correct.get_db().drop_collection("test_inventory")
    test_db_correct.set_collection("test_inventory")
    test_db_correct.insert_item(test_item_one)

    assert test_db_correct.update_item(1, name="hehe") == 1
    assert test_db_correct.update_item(1, name="heh2", sell_in=2) == 1
    assert test_db_correct.update_item(1, name="hehasd3415", sell_in=2, quality=3) == 1
    assert (
        test_db_correct.update_item(
            1, name="heh3415", sell_in=2, quality=3, item_type="Sulfuras"
        )
        == 1
    )

    assert (
        test_db_correct.update_item(
            1, name="heh3415", sell_in=2, quality=3, typ2="Sulfuras"
        )
        == 0
    )
    assert test_db_correct.update_item(2) == 0

# This test the mechanism, but to keep the database at time. I will not implement it, otherwise it initate the data everytime.
# @pytest.mark.test_init_db
# def test_init_db(test_db_correct):
#     test_db_correct.set_collection("items")
#     test_db_correct.update_item(1, name="hehe")
#     assert test_db_correct.inventory() != items_day_zero
#     Database.init_db()
#     assert test_db_correct.inventory() == items_day_zero
