import unittest
from coe_number.funny_string import funnyString

class FunnyStringTest(unittest.TestCase):
    def test_give_acxz_should_be_funny(self):
        # Arrange
        s = "acxz"
        # Act
        result = funnyString(s)
        # Assert
        self.assertEqual(result, "Funny")

    def test_give_bcxz_should_be_not_funny(self):
        self.assertEqual(funnyString("bcxz"), "Not Funny")

    def test_give_ab_should_be_funny(self):
        self.assertEqual(funnyString("ab"), "Funny")

    def test_give_zzzz_should_be_funny(self):
        self.assertEqual(funnyString("zzzz"), "Funny")

    def test_give_adfg_should_be_not_funny(self):
        self.assertEqual(funnyString("adfg"), "Not Funny")

if __name__ == '__main__':
    unittest.main()