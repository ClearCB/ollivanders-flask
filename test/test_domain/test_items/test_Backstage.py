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

    check_sell_in = 13
    check_quality = 40
    for i in range(0,15):

        if 5 < check_sell_in <= 10:

            check_quality += 2
        
        elif 0 < check_sell_in <= 5:

            check_quality += 3

        elif check_sell_in <= 0:

            check_quality = 0

        if check_quality >= 50:

            check_quality = 50

        backstage.update_quality()
        check_sell_in -= 1
        assert check_quality == backstage.quality
        assert check_sell_in == backstage.sell_in
