#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)
    def test_negative(self):
        result = max_integer([-2, -3, -1, -4])
        self.assertEqual(result, -1)
    def test_None(self):
        result = max_integer([])
        self.assertEqual(result, None)
    def test_only(self):
        result = max_integer([94])
        self.assertEqual(result, 94)
