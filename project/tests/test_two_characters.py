import unittest
from coe_number.two_characters import alternate

class TwoCharactersTest(unittest.TestCase):
    def test_give_beabeefeab_should_be_5(self):
        # Arrange
        s = "beabeefeab"
        # Act
        result = alternate(s)
        # Assert
        self.assertEqual(result, 5)

    def test_give_aab_should_be_0(self):
        self.assertEqual(alternate("aab"), 0)

    def test_give_single_char_should_be_0(self):
        self.assertEqual(alternate("a"), 0)

    def test_give_abab_should_be_4(self):
        self.assertEqual(alternate("abab"), 4)

    def test_give_aabbaa_should_be_0(self):
        self.assertEqual(alternate("aabbaa"), 0)

