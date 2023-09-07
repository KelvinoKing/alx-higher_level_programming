#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_empty_list(self):
        """Test when the input list is empty."""
        result = max_integer([])
        self.assertIsNone(result, "Expected None for an empty list")

    def test_non_list_parameter(self):
        """Test when param is not a list"""
        with self.assertRaises(TypeError):
            max_integer(2)

    def test_positive_numbers(self):
        """Test when the input list contains positive numbers."""
        result = max_integer([1, 3, 5, 2, 4])
        self.assertEqual(result, 5, "Expected 5 as the maximum integer")

    def test_negative_numbers(self):
        """Test when the input list contains negative numbers."""
        result = max_integer([-1, -3, -5, -2, -4])
        self.assertEqual(result, -1, "Expected -1 as the maximum integer")

    def test_mixed_numbers(self):
        """Test when the input list contains mixed numbers."""
        result = max_integer([-1, 3, 0, 2, -4])
        self.assertEqual(result, 3, "Expected 3 as the maximum integer")

    def test_list_with_single_element(self):
        """Test when the input list contains a single element."""
        result = max_integer([42])
        self.assertEqual(result, 42, "Expected 42 as the maximum integer")

    def test_list_with_non_integer_elements(self):
        """Test when the input list contains non-integer elements."""
        with self.assertRaises(TypeError):
            max_integer([1, 3, "2", True, "apple"])
