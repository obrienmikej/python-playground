import pytest
from src.remove_element import removeElement, removeElementTwoPointers

@pytest.mark.parametrize("func", [removeElement, removeElementTwoPointers])
def test_remove_element_one_occurance(func):
    nums = [3, 2, 2]
    val =  3
    k = func(nums, val)
    assert sorted(nums[:k]) == [2, 2]

@pytest.mark.parametrize("func", [removeElement, removeElementTwoPointers])
def test_remove_element_multiple_occurnaces(func):
    nums = [3, 2, 2, 3]
    val =  3
    k = func(nums, val)
    assert sorted(nums[:k]) == [2, 2]

@pytest.mark.parametrize("func", [removeElement, removeElementTwoPointers])
def test_remove_element_empty_array(func):
    nums = []
    val =  1
    k = func(nums, val)
    assert sorted(nums[:k]) == []

@pytest.mark.parametrize("func", [removeElement, removeElementTwoPointers])
def test_remove_element_no_occurance(func):
    nums = [1, 2, 3, 4, 5]
    val =  6
    k = func(nums, val)
    assert sorted(nums[:k]) == [1, 2, 3, 4, 5]

@pytest.mark.parametrize("func", [removeElement, removeElementTwoPointers])
def test_remove_element_all(func):
    nums = [1, 1, 1]
    val =  1
    k = func(nums, val)
    assert sorted(nums[:k]) == []
   