from resources.Items import Items
from services.Services import Services
import pytest

@pytest.fixture
def items():
    return Items()


@pytest.mark.test_inventario
def test_inventario(items):

    Services.delete_one(0)
    Services.create_one(0, name="Sulfutas", sell_in=1, quality=1, item_type="Sulfuras")
    item = {
        "_id": 0,
        "name": "Sulfutas",
        "sell_in": 1,
        "quality": 1,
        "item_type": "Sulfuras",
    }

    assert items.get(0)[1] == 200
    assert items.get(0)[0] == item

