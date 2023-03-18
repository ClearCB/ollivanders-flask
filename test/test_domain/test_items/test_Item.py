from domain.items.Item import Item
import pytest


@pytest.mark.test_repr
def test_repr():
    item = Item("New", 10, 10)
    assert repr(item) == "New 10 10"
