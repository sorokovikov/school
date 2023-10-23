from unittest import TestCase

from recursion.task_2 import sum_number_digits


class TestSum(TestCase):

    def test_sum(self):

        self.assertEqual(10, sum_number_digits(28))
        self.assertEqual(18, sum_number_digits(723051))
        self.assertEqual(55, sum_number_digits(851724912457))
        self.assertEqual(1, sum_number_digits(10000000000))
