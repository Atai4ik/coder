# coding: utf-8

import unittest
from script import fizz_buzz


class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz_zero(self):
        self.assertEqual(fizz_buzz(0), 'SmallInt')

    def test_string(self):
        self.assertEqual(fizz_buzz("Hello"), 'StringError')

    def test_fizz(self):
        self.assertEqual(fizz_buzz(3), 'Fizz')

    def test_buzz(self):
        self.assertEqual(fizz_buzz(5), 'Buzz')

    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz(15), 'FizzBuzz')


if __name__ == '__main__':
    unittest.main()
