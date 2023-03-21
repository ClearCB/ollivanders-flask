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

    error_get_item = {"ERROR":"Item not found. Check the data and try again."}

    response = client.get("/items/find-one/0")
    item = {
        "_id": 0,
        "name": "test_item",
        "sell_in": 5,
        "quality": 10,
        "item_type": "NormalItem",
    }
    assert response.json == item

    response = client.get("/items/find-one/sdg")
    assert response.json == error_get_item

    response = client.get("/items/find-one/126547")
    assert response.json == error_get_item

@pytest.mark.test_delete_item
def test_delete_item(client):

    error_delete_item = {"ERROR":"Item not found. Check the data and try again."}

    response = client.delete("/items/delete-one/0")
    assert response.json == {"Item id deleted": "0"}
    assert response.status_code == 200

    response = client.delete("/items/delete-one/3ssr")

    assert response.json == error_delete_item
    response = client.delete("/items/delete-one/0")
    assert response.json == error_delete_item


@pytest.mark.test_update_item
def test_update_item(client):

    error_update_item = {"ERROR":"Please, update action not posible. Check the data and try again"}

    update_statement = {
        "sell_in":8
    }
    response = client.put("/items/update-one/0", json=update_statement)
    assert response.status_code == 200
    assert response.json == {"Item id updated":"0"}

    update_statement = {
        "sell_in":"36sad"
    }
    response = client.put("/items/update-one/0", json=update_statement)

    assert response.json == error_update_item



@pytest.mark.test_create_item
def test_create_item(client):

    item = {
        "_id": 1000000,
        "name": "test_item",
        "sell_in": 5,
        "quality": 10,
        "item_type": "NormalItem",
    }
    response = client.post("/items/create-item",json=item)

    assert response.status_code == 200
    assert response.json == {"Item created with id":1000000}

    response = client.post("/items/create-item",json={"haha":24})

    assert response.json == {"ERROR": "The item could not be inserted"}