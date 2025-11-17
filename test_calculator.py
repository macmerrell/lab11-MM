# https://github.com/macmerrell/lab11-MM
# Partner 1: Matthew Merrell
# Partner 2: Matthew Merrell

import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        result1 = calculator.add(1, 1)
        self.assertEqual(result1, 2)

        result2 = calculator.add(-5, 5)
        self.assertEqual(result2, 0)

        result3 = calculator.add(10, -3)
        self.assertEqual(result3, 7)

    def test_subtract(self):
        result1 = calculator.sub(5, 3)
        self.assertEqual(result1, 2)

        result2 = calculator.sub(0, 5)
        self.assertEqual(result2, -5)

        result3 = calculator.sub(-4, -6)
        self.assertEqual(result3, 2)

    def test_multiply(self):
        result1 = calculator.mul(2, 3)
        self.assertEqual(result1, 6)

        result2 = calculator.mul(-4, 5)
        self.assertEqual(result2, -20)

        result3 = calculator.mul(0, 999)
        self.assertEqual(result3, 0)

    def test_divide(self):
        result1 = calculator.div(2, 10)
        self.assertAlmostEqual(result1, 5)

        result2 = calculator.div(5, 20)
        self.assertAlmostEqual(result2, 4)

        result3 = calculator.div(4, -12)
        self.assertAlmostEqual(result3, -3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    def test_logarithm(self):
        result1 = calculator.log(10, 100)
        self.assertAlmostEqual(result1, 2)

        result2 = calculator.log(2, 8)
        self.assertAlmostEqual(result2, 3)

        result3 = calculator.log(3, 9)
        self.assertAlmostEqual(result3, 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.log(1, 10)


    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.log(-2, 10)

    def test_hypotenuse(self):
        result1 = calculator.hypotenuse(3, 4)
        self.assertAlmostEqual(result1, 5)

        result2 = calculator.hypotenuse(5, 12)
        self.assertAlmostEqual(result2, 13)

        result3 = calculator.hypotenuse(0, 7)
        self.assertAlmostEqual(result3, 7)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            calculator.square_root(-9)

        result1 = calculator.square_root(4)
        self.assertAlmostEqual(result1, 2)

        result2 = calculator.square_root(16)
        self.assertAlmostEqual(result2, 4)


if __name__ == "__main__":
    unittest.main()
