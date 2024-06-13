from src.remove_element import removeElement
from src.remove_element import removeElementTwoPointers

def test_remove_element_one_occurance():
    nums = [3, 2, 2]
    val =  3
    k = removeElement(nums, val)
    assert sorted(nums[:k]) == [2, 2]

def test_remove_element_two_pointers_one_occurance():
    nums = [3, 2, 2]
    val =  3
    k = removeElementTwoPointers(nums, val)
    assert sorted(nums[:k]) == [2, 2]

def test_remove_element_multiple_occurnaces():
    nums = [3, 2, 2, 3]
    val =  3
    k = removeElement(nums, val)
    assert sorted(nums[:k]) == [2, 2]

def test_remove_element_two_pointers_multiple_occurnaces():
    nums = [3, 2, 2, 3]
    val =  3
    k = removeElementTwoPointers(nums, val)
    assert sorted(nums[:k]) == [2, 2]  

def test_remove_element_empty_array():
    nums = []
    val =  1
    k = removeElement(nums, val)
    assert sorted(nums[:k]) == []

def test_remove_element_two_pointers_empty_array():
    nums = []
    val =  1
    k = removeElementTwoPointers(nums, val)
    assert sorted(nums[:k]) == []

def test_remove_element_no_occurance():
    nums = [1, 2, 3, 4, 5]
    val =  6
    k = removeElement(nums, val)
    assert sorted(nums[:k]) == [1, 2, 3, 4, 5]

def test_remove_element_two_pointers_no_occurance():
    nums = [1, 2, 3, 4, 5]
    val =  6
    k = removeElementTwoPointers(nums, val)
    assert sorted(nums[:k]) == [1, 2, 3, 4, 5]

def test_remove_element_all():
    nums = [1, 1, 1]
    val =  1
    k = removeElement(nums, val)
    assert sorted(nums[:k]) == []

def test_remove_element_two_pointers_all():
    nums = [1, 1, 1]
    val =  1
    k = removeElementTwoPointers(nums, val)
    assert sorted(nums[:k]) == []
   