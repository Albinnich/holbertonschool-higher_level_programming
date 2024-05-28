import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Defines unittests for max_integer function"""

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_negative_number(self):
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_positive_and_negative(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_single_element(self):
        self.assertEqual(max_integer([1]), 1)

if __name__ == '__main__':
    unittest.main()
