import pytest
from app import init_app


@pytest.fixture()
def app():

    app = init_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    yield app


@pytest.fixture()
def client(app):

    return app.test_client()


@pytest.fixture()
def runner(app):

    return app.test_cli_runner()


@pytest.mark.test_get_item
def test_get_item(client):

    response = client.get("/items/find-one/0")
    item = {
        "_id": 0,
        "name": "test_item",
        "sell_in": 5,
        "quality": 10,
        "item_type": "NormalItem",
    }
    assert response.json == item


@pytest.mark.test_delete_item
def test_delete_item(client):

    response = client.delete("/items/delete-one/0")
    m = {"Item id deleted": "0"}

    assert response.json == m
    assert response.status_code == 200

    response = client.delete("/items/delete-one/0")

    error = {"ERROR": "Item not found"}

    assert response.status_code == 200
    assert response.json == error


@pytest.mark.test_update_item
def test_update_item(client):

    item = {
        "_id": 0,
        "name": "test_item",
        "sell_in": 5,
        "quality": 10,
        "item_type": "NormalItem",
    }
    update_statement = {
        "sell_in":8
    }

    response = client.update(0,update_statement)

    assert response.status_code == 200
    assert response.json == {"Item id updated":"0"}

@pytest.mark.test_create_item
def test_create_item(client):

    item = {
        "_id": 1000000,
        "name": "test_item",
        "sell_in": 5,
        "quality": 10,
        "item_type": "NormalItem",
    }

    response = client.post("/items/create-one/",json=item)


    assert response.status_code == 200
    assert response.json == {"_id":1000000}

