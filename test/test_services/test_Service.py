from services.Services import Services
from repository.Database import Database
import pytest


@pytest.mark.test_create_one
def test_create_one():

    Services.delete_one(10000)
    assert (
        Services.create_one(
            10000, name="Sulfutas", sell_in=1, quality=1, item_type="Sulfuras"
        ).inserted_id
        == 10000
    )
    Services.delete_one(10000)


@pytest.mark.test_get_one
def test_get_one():

    Services.create_one(
        10000, name="Sulfutas", sell_in=1, quality=1, item_type="Sulfuras"
    )
    item = {
        "_id": 10000,
        "name": "Sulfutas",
        "sell_in": 1,
        "quality": 1,
        "item_type": "Sulfuras",
    }

    assert Services.get_one(10000) == item
    Services.delete_one(10000)


@pytest.mark.test_get_inventory
def test_get_inventory():

    Services.create_one(
        10000, name="Sulfutas", sell_in=1, quality=1, item_type="Sulfuras"
    )
    assert isinstance(Services.inventory(), list)
    assert isinstance(Services.inventory()[0], dict)
    assert Database.correct_item(Services.inventory()[0])

    Services.delete_one(10000)


@pytest.mark.test_update_one
def test_update_one():

    Services.create_one(
        10000, name="Sulfutas", sell_in=1, quality=1, item_type="Sulfuras"
    )
    assert Services.update_one(10000, name="haha") == 1

    item = {
        "_id": 10000,
        "name": "haha",
        "sell_in": 1,
        "quality": 1,
        "item_type": "Sulfuras",
    }

    assert Services.get_one(10000) == item

    Services.delete_one(10000)


@pytest.mark.test_delete_one
def test_delete_one():

    assert Services.delete_one(10000) == 1
