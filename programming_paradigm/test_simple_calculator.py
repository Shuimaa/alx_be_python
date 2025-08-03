import unittest
from programming_paradigm.simple_calculator import SimpleCalculator  # ✅ مهم جداً

class TestSimpleCalculator(unittest.TestCase):
    def test_add(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.add(2, 3), 5)

    def test_subtract(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.subtract(5, 2), 3)

    def test_multiply(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.multiply(4, 3), 12)

    def test_divide(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            calc.divide(5, 0)

if __name__ == '__main__':
    unittest.main()
