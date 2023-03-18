from resources.Inventario import Inventario
import pytest

@pytest.fixture
def inventario():

    return Inventario()

@pytest.mark.test_inventario
def test_inventario(inventario):

    assert isinstance(inventario.get()[0],list)
    assert inventario.get()[1] == 200

    assert inventario.post() == None