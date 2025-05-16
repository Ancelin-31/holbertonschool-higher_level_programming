#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer function"""

    def test_ordered_list(self):
        """Test a list of ordered integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list of unordered integers"""
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)

    def test_single_element(self):
        """Test a list with a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test a list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test a list with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 0, 3, -4]), 3)

    def test_floats(self):
        """Test a list with float numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 2.0]), 3.5)

    def test_mixed_types(self):
        """Test a list with integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 2.0]), 3)

    def test_string(self):
        """Test a string as input"""
        self.assertEqual(max_integer("hello"), "o")

    def test_list_of_strings(self):
        """Test a list of strings"""
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_none(self):
        """Test None as input"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_iterable(self):
        """Test a non-iterable input"""
        with self.assertRaises(TypeError):
            max_integer(123)

if __name__ == "__main__":
    unittest.main()
