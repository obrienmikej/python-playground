from src.remove_element import removeElement
from src.remove_element import removeElementTwoPointers


def test_remove_element_one_occurance():
    nums = [3, 2, 2]
    remove = 3
    nums_expected = [2, 2]
    r = removeElement(nums, remove)
    assert sorted(nums[:r]) == nums_expected

def test_remove_element_two_pointers_one_occurance():
    nums = [3, 2, 2]
    remove = 3
    nums_expected = [2, 2]
    r = removeElementTwoPointers(nums, remove)
    assert sorted(nums[:r]) == nums_expected

def test_remove_element_multiple_occurnaces():
    nums = [3, 2, 2, 3]
    remove = 3
    nums_expected = [2, 2]
    r = removeElement(nums, remove)
    assert sorted(nums[:r]) == nums_expected

def test_remove_element_two_pointers_multiple_occurnaces():
    nums = [3, 2, 2, 3]
    remove = 3
    nums_expected = [2, 2]
    r = removeElementTwoPointers(nums, remove)
    assert sorted(nums[:r]) == nums_expected    

def test_remove_element_empty_array():
    nums = []
    remove = 1
    nums_expected = []
    r = removeElement(nums, remove)
    assert sorted(nums[:r]) == nums_expected

def test_remove_element_two_pointers_empty_array():
    nums = []
    remove = 1
    nums_expected = []
    r = removeElementTwoPointers(nums, remove)
    assert sorted(nums[:r]) == nums_expected

def test_remove_element_no_occurance():
    nums = [1, 2, 3, 4, 5]
    remove = 6
    nums_expected = [1, 2, 3, 4, 5]
    r = removeElement(nums, remove)
    assert sorted(nums[:r]) == nums_expected

def test_remove_element_two_pointers_no_occurance():
    nums = [1, 2, 3, 4, 5]
    remove = 6
    nums_expected = [1, 2, 3, 4, 5]
    r = removeElementTwoPointers(nums, remove)
    assert sorted(nums[:r]) == nums_expected    

def test_remove_element_all():
    nums = [1, 1, 1]
    remove = 1
    nums_expected = []
    r = removeElement(nums, remove)
    assert sorted(nums[:r]) == nums_expected

def test_remove_element_two_pointers_all():
    nums = [1, 1, 1]
    remove = 1
    nums_expected = []
    r = removeElementTwoPointers(nums, remove)
    assert sorted(nums[:r]) == nums_expected
   