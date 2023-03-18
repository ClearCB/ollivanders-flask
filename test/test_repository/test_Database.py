from pymongo import MongoClient
import pytest


# Creating an aditional collection / database to the test.
@pytest.fixture
def test_db_correct():

    test_ollivanders_database_correct = Database("URI")
    test_ollivanders_database_correct.connect()
    return test_ollivanders_database_correct


@pytest.fixture
def test_db_not_correct():

    test_ollivanders_database_incorrect = Database("URI")
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
def test_db_connection(test_db_correct, test_db_not_correct):

    assert test_db_correct.connect() == "The connection was succesfull!"
    assert (
        test_db_not_correct.connect()
        == "The connection was not posible, please. Check the data and try again"
    )


@pytest.mark.test_get_database
def test_get_database(test_db_correct, test_db_not_correct):

    assert isinstance(test_db_correct.database(), MongoClient)
    assert test_db_not_correct.database() == None


@pytest.mark.test_insert_item
def test_insert_item(test_db_correct, test_item_one, test_item_two):

    assert test_db_correct.insert_item(test_item_one).inserted_id == 1
    assert test_db_correct.insert_item(test_item_two).inserted_id == 2


@pytest.mark.test_get_inventory
def test_get_inventory(test_db_correct):

    inventory_test = [
        {"_id": 1, "name": "Aged Brie", "sell_in": 10, "quality": 30},
        {"_id": 2, "name": "Aged Brie", "sell_in": 10, "quality": 30},
    ]

    assert test_db_correct.inventory() == inventory_test
