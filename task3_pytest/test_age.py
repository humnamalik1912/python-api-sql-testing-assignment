import pytest
from age import is_adult


# Test case 1: Age 17
def test_age_17():
    assert is_adult(17) == False


# Test case 2: Age 18
def test_age_18():
    assert is_adult(18) == True


# Test case 3: Negative age
def test_age_negative():
    with pytest.raises(ValueError):
        is_adult(-1)