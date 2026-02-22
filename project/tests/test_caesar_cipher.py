import unittest
from coe_number.caesar_cipher import caesarCipher

class CaesarCipherTest(unittest.TestCase):
    def test_give_middle_outz_shift_2(self):
        # Arrange
        s = "middle-Outz"
        k = 2
        # Act
        result = caesarCipher(s, k)
        # Assert
        self.assertEqual(result, "okffng-Qwvb")

    def test_give_abc_shift_3(self):
        self.assertEqual(caesarCipher("abc", 3), "def")

    def test_give_XYZ_shift_5(self):
        self.assertEqual(caesarCipher("XYZ", 5), "CDE")

    def test_give_abc_shift_26(self):
        self.assertEqual(caesarCipher("abc", 26), "abc")

    def test_give_symbols_shift_4(self):
        self.assertEqual(caesarCipher("1234-5678!", 4), "1234-5678!")

if __name__ == '__main__':
    unittest.main()