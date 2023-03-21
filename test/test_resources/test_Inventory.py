import pytest
from app import init_app

@pytest.fixture()
def app():

    app = init_app()
    app.config.update({
        "TESTING":True,
    })

    yield app

@pytest.fixture()
def client(app):

    return app.test_client()

@pytest.fixture()
def runner(app):

    return app.test_cli_runner()


@pytest.mark.test_inventory
def test_inventory(client):

    response = client.get("/inventory")
    item = {
        "_id":0,
        "name":"test_item",
        "sell_in":5,
        "quality":10,
        "item_type":"NormalItem"
    }
    
    assert response.status_code == 200
    assert item in response.json 