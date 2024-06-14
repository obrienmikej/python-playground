import unittest
from src.merge_two_sorted_lists import *

class TestMergeTwoLists(unittest.TestCase):
    def test_merge_two_sorted_lists(self):
        list1 = create_linked_list([1, 2, 4])
        list2 = create_linked_list([1, 3, 4])
        expected_output = [1, 1, 2, 3, 4, 4]
        merged_list = mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(merged_list), expected_output)
    
    def test_merge_two_empty_lists(self):
        list1 = create_linked_list([])
        list2 = create_linked_list([])
        expected_output = []
        merged_list = mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(merged_list), expected_output)

    def test_merge_one_empty_and_one_non_empty_list(self):
        list1 = create_linked_list([])
        list2 = create_linked_list([0])
        expected_output = [0]
        merged_list = mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(merged_list), expected_output)

    def test_merge_two_single_element_lists(self):
        list1 = create_linked_list([1])
        list2 = create_linked_list([2])
        expected_output = [1, 2]
        merged_list = mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(merged_list), expected_output)

    def test_merge_one_single_element_and_one_multi_element_list(self):
        list1 = create_linked_list([5])
        list2 = create_linked_list([1, 2, 3, 4])
        expected_output = [1, 2, 3, 4, 5]
        merged_list = mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(merged_list), expected_output)