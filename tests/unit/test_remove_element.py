from src.remove_element import removeElementOptionA
from src.remove_element import removeElementOptionB


def test_optionA_remove_element_one_occurance():
    nums = [3, 2, 2]
    remove = 3
    nums_expected = [2, 2]
    r = removeElementOptionA(nums, remove)
    assert sorted(nums[:r]) == nums_expected

def test_optionB_remove_element_one_occurance():
    nums = [3, 2, 2]
    remove = 3
    nums_expected = [2, 2]
    r = removeElementOptionB(nums, remove)
    assert sorted(nums[:r]) == nums_expected

def test_remove_element_multiple_occurnaces():
    nums = [3, 2, 2, 3]
    remove = 3
    nums_expected = [2, 2]
    r = removeElementOptionA(nums, remove)
    assert sorted(nums[:r]) == nums_expected

def test_remove_element_empty_array():
    nums = []
    remove = 1
    nums_expected = []
    r = removeElementOptionA(nums, remove)
    assert sorted(nums[:r]) == nums_expected

def test_remove_element_no_occurance():
    nums = [1, 2, 3, 4, 5]
    remove = 6
    nums_expected = [1, 2, 3, 4, 5]
    r = removeElementOptionA(nums, remove)
    assert sorted(nums[:r]) == nums_expected

def test_remove_element_all():
    nums = [1, 1, 1]
    remove = 1
    nums_expected = []
    r = removeElementOptionA(nums, remove)
    assert sorted(nums[:r]) == nums_expected