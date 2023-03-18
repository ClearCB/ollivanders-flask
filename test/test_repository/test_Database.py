from repository.Database import Database
from pymongo import MongoClient
import os
import pytest


# Creating an aditional collection / database to the test.
@pytest.fixture
def test_db_correct():

    test_ollivanders_database_correct = Database(os.environ["MONGO_ATLAS_URI"])
    test_ollivanders_database_correct.connect()
    return test_ollivanders_database_correct


@pytest.fixture
def test_db_not_correct():

    test_ollivanders_database_incorrect = Database("hellothisisnotgoingtowork")
    test_ollivanders_database_incorrect.connect()
    return test_ollivanders_database_incorrect


@pytest.fixture
def test_item_one():

    item = {"_id": 1, "name": "Aged Brie", "sell_in": 10, "quality": 30}
    return item


@pytest.fixture
def test_item_two():

    item = {"_id": 2, "name": "Aged Brie", "sell_in": 10, "quality": 30}
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


@pytest.mark.test_get_client
def test_get_client(test_db_correct, test_db_not_correct):

    assert isinstance(test_db_correct.client, MongoClient)
    assert test_db_not_correct.client == None

@pytest.mark.test_get_database
def test_get_databaase(test_db_correct):

    assert test_db_correct.get_db() == test_db_correct.client["ollivander_shop"]


@pytest.mark.test_correct_item
def test_correct_item(test_item_one, test_item_two):

    item = {"_id": 2, "name": "Aged Brie", "sell_in": Database("s"), "quality": 30}

    assert Database.correct_item(test_item_one)
    assert Database.correct_item(test_item_two) 
    assert Database.correct_item(item) == False
    assert Database.correct_item(["AHHS"]) == False
    assert Database.correct_item(1) == False


@pytest.mark.test_insert_item
def test_insert_item(test_db_correct, test_item_one, test_item_two):

    test_db_correct.get_db().drop_collection("inventory")

    assert test_db_correct.insert_item(test_item_one).inserted_id == 1
    assert test_db_correct.insert_item(test_item_two).inserted_id == 2


# @pytest.mark.test_get_inventory
# def test_get_inventory(test_db_correct):

#     inventory_test = [
#         {"_id": 1, "name": "Aged Brie", "sell_in": 10, "quality": 30},
#         {"_id": 2, "name": "Aged Brie", "sell_in": 10, "quality": 30},
#     ]

#     assert test_db_correct.inventory() == inventory_test
