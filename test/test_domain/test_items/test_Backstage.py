from domain.items.Backstage import Backstage
import pytest

'''
Test the item Backstage
'''

# Fixture to create an object
@pytest.fixture
def backstage():

    test_backstage = Backstage("Backstage", 13, 40)

    return test_backstage

# Test the updateQuality method
@pytest.mark.test_update_quality
def test_update_quality(backstage):

    # Day zero
    assert backstage.sell_in == 13
    assert backstage.quality == 40    
    backstage.update_quality()
    
    # Day one
    assert backstage.sell_in == 12
    assert backstage.quality == 41
    backstage.update_quality()
    
    # Day two
    assert backstage.sell_in == 11
    assert backstage.quality == 42
    backstage.update_quality()
    
    # Day three
    assert backstage.sell_in == 10
    assert backstage.quality == 43
    backstage.update_quality()
    
    # Day four
    assert backstage.sell_in == 9
    assert backstage.quality == 45
    backstage.update_quality()
    
    # Day five
    assert backstage.sell_in == 8
    assert backstage.quality == 47
    backstage.update_quality()
    
    # Day six
    assert backstage.sell_in == 7
    assert backstage.quality == 49
