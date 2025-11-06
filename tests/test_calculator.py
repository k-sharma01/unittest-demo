import unittest
from src import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_normal(self):
        self.assertEqual(self.calc.add(5, 8), 13)

    def test_subtract_normal(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_multiply_normal(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_divide_normal(self):
        self.assertEqual(self.calc.divide(20, 4), 5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
