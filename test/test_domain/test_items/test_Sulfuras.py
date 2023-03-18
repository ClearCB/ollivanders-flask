from domain.items.Sulfuras import Sulfuras
import pytest

"""
This module will check the legendary item sulfuras. And its quality behaviour.
"""


@pytest.fixture
def sulfur():
    test_sulfuras = Sulfuras("Sulfuras", 10, 80)

    return test_sulfuras


@pytest.mark.test_update_quality
def test_update_quality(sulfur):
    # Day zero
    assert sulfur.sell_in == 10
    assert sulfur.quality == 80
    sulfur.update_quality()

    # Day one
    assert sulfur.sell_in == 10
    assert sulfur.quality == 80
    sulfur.update_quality()

    # Day two
    assert sulfur.sell_in == 10
    assert sulfur.quality == 80
    sulfur.update_quality()

    # Day three
    assert sulfur.sell_in == 10
    assert sulfur.quality == 80
    sulfur.update_quality()

    # Day four
    assert sulfur.sell_in == 10
    assert sulfur.quality == 80
    sulfur.update_quality()

    # Day five
    assert sulfur.sell_in == 10
    assert sulfur.quality == 80
    sulfur.update_quality()

    # Day six
    assert sulfur.sell_in == 10
    assert sulfur.quality == 80
