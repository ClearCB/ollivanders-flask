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

    response = client.delete("/items/delete-one/0")

    error = {"error": "Item not found"}

    assert response.json == error
