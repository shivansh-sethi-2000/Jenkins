#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Prog1 import summation

class TestAvg(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = [23, 32]
        result = Average(data)
        self.assertEqual(result, 55)

if __name__ == '__main__':
    unittest.main()
