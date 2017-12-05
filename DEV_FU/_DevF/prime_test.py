import unittest
#import prime
from prime import is_prime


class PrimeTest(unittest.TestCase):

    def setUp(self):
        self.x =5

    def test_5_is_prime(self):
        self.assertTrue(is_prime(5))
    def test_5_is_prime(self):
        self.assertTrue(is_prime(4))
    def test_5_is_prime(self):
        self.assertTrue(is_prime(5))

if __name__ == "__main__":
    unittest.main()