import unittest
from calculator import Calculator


class UnitTest(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(Calculator(2, 3).addition(), 5)
        self.assertEqual(Calculator(-1, 3).addition(), 2)
        self.assertEqual(Calculator(-1, -1).addition(), -2)

    def test_subtract(self):
        self.assertEqual(Calculator(2, 3).subtract(), -1)
        self.assertEqual(Calculator(-1, 3).subtract(), -4)
        self.assertEqual(Calculator(-1, -1).subtract(), 0)

    def test_multiply(self):
        self.assertEqual(Calculator(2, 3).multiply(), 6)
        self.assertEqual(Calculator(2, -3).multiply(), -6)
        self.assertEqual(Calculator(2, 0).multiply(), 0)

    def test_divide(self):
        self.assertEqual(Calculator(3, 2).divide(), 1.5)
        self.assertEqual(Calculator(2, -1).divide(), -2)


if __name__ == "__main__":
    unittest.main()
