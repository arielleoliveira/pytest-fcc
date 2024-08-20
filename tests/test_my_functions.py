from operator import truediv

import pytest
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(number_one=1, number_two=2)
    assert result == 3

def test_add_string():
    result = my_functions.add("I like ","burgers")
    assert result == "I like burgers"

def test_divide():
    result = my_functions.divide(number_one=1, number_two=2)
    assert result == 0.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(number_one=1, number_two=0)