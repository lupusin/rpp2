import unittest
from discriminant import calculate_discriminant


class TestDiscriminant(unittest.TestCase):
    # Позитивные тесты
    def test_positive_discriminant(self):
        self.assertEqual(calculate_discriminant(1, -3, 2), 1)  # D > 0

    def test_zero_discriminant(self):
        self.assertEqual(calculate_discriminant(1, -2, 1), 0)  # D = 0

    # Негативные тесты
    def test_negative_discriminant(self):
        self.assertEqual(calculate_discriminant(1, 2, 5), -16)  # D < 0


if __name__ == "__main__":
    unittest.main()