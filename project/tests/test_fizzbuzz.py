import unittest
from coe_number.fizzbuzz import fizzbuzz

class FizzBuzzTest(unittest.TestCase):
    def test_give_3_should_return_fizz(self):
        # Arrange
        number = 3
        # Act
        result = fizzbuzz(number)
        # Assert
        self.assertEqual(result, "Fizz")

    def test_give_5_should_return_buzz(self):
        number = 5
        result = fizzbuzz(number)
        self.assertEqual(result, "Buzz")

    def test_give_15_should_return_fizzbuzz(self):
        number = 15
        result = fizzbuzz(number)
        self.assertEqual(result, "FizzBuzz")

    def test_give_2_should_return_2_string(self):
        number = 2
        result = fizzbuzz(number)
        self.assertEqual(result, "2")

