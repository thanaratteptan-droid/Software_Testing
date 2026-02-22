import unittest
from coe_number.alternating_characters import alternatingCharacters

class AlternatingCharactersTest(unittest.TestCase):
    def test_give_AAAA_should_be_3(self):
        # Arrange
        s = "AAAA"
        # Act
        result = alternatingCharacters(s)
        # Assert
        self.assertEqual(result, 3)

    def test_give_BBBBB_should_be_4(self):
        self.assertEqual(alternatingCharacters("BBBBB"), 4)

    def test_give_ABABABAB_should_be_0(self):
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)

    def test_give_AAABBB_should_be_4(self):
        self.assertEqual(alternatingCharacters("AAABBB"), 4)

    def test_give_empty_string_should_be_0(self):
        self.assertEqual(alternatingCharacters(""), 0)

