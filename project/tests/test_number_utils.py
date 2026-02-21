import unittest
from coe_number.number_utils import is_prime_list

class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_4_6_8_is_not_prime(self):
        prime_list = [4, 6, 8] 
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_5_is_prime(self):
        prime_list = [5]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_empty_list(self):
        prime_list = []
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_negative_primes(self):
        prime_list = [-2, -3]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

if __name__ == '__main__':
    unittest.main()