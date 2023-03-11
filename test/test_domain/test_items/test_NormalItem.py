from domain.items.NormalItem import NormalItem
import pytest

'''
This module will check an unitary test from the NormalItem class.
'''

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

    check_quality = 10 # The quality starts at 10
    check_sell_in = 5
    # We make a loop to count 11 days and see if the quality is having a correctly behaviour
    for i in range(0,12):

        # If the sellin is negative, decreases 2
        if check_sell_in < 0:
            check_quality -= 2
        
        # if the quality is negative, it returns to 0
        if check_quality < 0:
            check_quality = 0

        # Else if, the quality decreases 1
        elif check_sell_in >= 0:
            check_quality -=1

        # We update de quality to the object
        mouse.update_quality()
        check_sell_in -= 1

        # We compare if both qualities have the same behaviour
        assert mouse.quality == check_quality
        assert mouse.sell_in == check_sell_in