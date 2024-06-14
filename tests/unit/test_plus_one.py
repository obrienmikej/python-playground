import unittest
from src.plus_one import plusOne

class TestPlusOne(unittest.TestCase):


    def test_single_digit(self):
        self.assertEqual(plusOne([0]), [1])
        self.assertEqual(plusOne([1]), [2])
        self.assertEqual(plusOne([9]), [1, 0])


    def test_multiple_digits(self):
        self.assertEqual(plusOne([1, 2, 3]), [1, 2, 4])
        self.assertEqual(plusOne([4, 3, 2, 1]), [4, 3, 2, 2])
        self.assertEqual(plusOne([9, 9]), [1, 0, 0])
        self.assertEqual(plusOne([2, 9, 9]), [3, 0, 0])
        self.assertEqual(plusOne([9, 8, 9]), [9, 9, 0])

# def test_large_numbers(self):
#     self.assertEqual(plusOne([9] * 100), [1] + [0] * 100)
#     self.assertEqual(plusOne([1] + [0] * 99), [1] + [0] * 98 + [1])

# def test_edge_cases(self):
#     self.assertEqual(plusOne([0]), [1])
#     self.assertEqual(plusOne([8, 9, 9, 9]), [9, 0, 0, 0])
#     self.assertEqual(plusOne([1, 0, 0, 0]), [1, 0, 0, 1])