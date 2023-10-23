from unittest import TestCase
from recursion.task_1 import pow


class TestPow(TestCase):

    def test_pow(self):

        self.assertEqual(1024, pow(2, 10))
        self.assertEqual(25, pow(5, 2))
        self.assertEqual(10100250000, pow(100500, 2))
        self.assertEqual(100000000, pow(-10, 8))
        self.assertEqual(-343, pow(-7, 3))
