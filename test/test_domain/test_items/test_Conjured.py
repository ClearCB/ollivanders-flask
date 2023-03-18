from domain.items.Conjured import Conjured
import pytest

"""
Test the class conjured
"""


@pytest.fixture
def conjured():
    test_conjur = Conjured("Conjured Cloth", 10, 30)

    return test_conjur


@pytest.mark.test_update_quality
def test_update_quality(conjured):
    # Day zero
    assert conjured.sell_in == 10
    assert conjured.quality == 30
    conjured.update_quality()

    # Day one
    assert conjured.sell_in == 9
    assert conjured.quality == 28
    conjured.update_quality()

    # Day two
    assert conjured.sell_in == 8
    assert conjured.quality == 26
    conjured.update_quality()

    # Day three
    assert conjured.sell_in == 7
    assert conjured.quality == 24
    conjured.update_quality()

    # Day four
    assert conjured.sell_in == 6
    assert conjured.quality == 22
    conjured.update_quality()

    # Day five
    assert conjured.sell_in == 5
    assert conjured.quality == 20
    conjured.update_quality()

    # Day six
    assert conjured.sell_in == 4
    assert conjured.quality == 18
