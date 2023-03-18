from domain.items.NormalItem import NormalItem
import pytest

"""
This module will check an unitary test from the NormalItem class.
"""


@pytest.fixture
def mouse():
    test_mouse = NormalItem("Mouse", 5, 10)

    return test_mouse

# We will test the method that change the quality itself.
@pytest.mark.test_set_quality
def test_set_quality(mouse):
    assert mouse.quality == 10

    mouse.set_quality(+2)

    # Check if added correctly
    assert mouse.quality == 12

    mouse.set_quality(-2)

    # Check if removed correctly
    assert mouse.quality == 10

    mouse.quality = 60

    mouse.set_quality(+1)

    # Check if cannot be more than 50
    assert mouse.quality == 50

    mouse.quality = 1

    mouse.set_quality(-2)

    # Check if cannot be less than 0
    assert mouse.quality == 0


# We will test the method that update the quality.
@pytest.mark.test_update_quality
def test_update_quality(mouse):
    # Day zero
    assert mouse.sell_in == 5
    assert mouse.quality == 10
    mouse.update_quality()

    # Day one
    assert mouse.sell_in == 4
    assert mouse.quality == 9
    mouse.update_quality()

    # Day two
    assert mouse.sell_in == 3
    assert mouse.quality == 8
    mouse.update_quality()

    # Day three
    assert mouse.sell_in == 2
    assert mouse.quality == 7
    mouse.update_quality()

    # Day four
    assert mouse.sell_in == 1
    assert mouse.quality == 6
    mouse.update_quality()

    # Day five
    assert mouse.sell_in == 0
    assert mouse.quality == 5
    mouse.update_quality()

    # Day six
    assert mouse.sell_in == -1
    assert mouse.quality == 3
