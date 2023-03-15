from domain.items.AgedBrie import AgedBrie
import pytest

"""
Unitary test to check if Aged Brie quality has the correct behaviour
"""

# Using a fixture to interact correctly with the class AgedBrie
@pytest.fixture
def cheese():

    test_cheese = AgedBrie("Cheese", 5, 10)

    return test_cheese


# Test the method that update the quality of the class AgedBrie adapted to its category.
@pytest.mark.test_update_quality
def test_update_quality(cheese):

    # Day zero
    assert cheese.sell_in == 5
    assert cheese.quality == 10    
    cheese.update_quality()
    
    # Day one
    assert cheese.sell_in == 4
    assert cheese.quality == 11
    cheese.update_quality()
    
    # Day two
    assert cheese.sell_in == 3
    assert cheese.quality == 12
    cheese.update_quality()
    
    # Day three
    assert cheese.sell_in == 2
    assert cheese.quality == 13
    cheese.update_quality()
    
    # Day four
    assert cheese.sell_in == 1
    assert cheese.quality == 14
    cheese.update_quality()
    
    # Day five
    assert cheese.sell_in == 0
    assert cheese.quality == 15
    cheese.update_quality()
    
    # Day six
    assert cheese.sell_in == -1
    assert cheese.quality == 17
