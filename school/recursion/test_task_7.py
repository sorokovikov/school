from unittest import TestCase

from recursion.task_7 import find_second_max


class TestFind(TestCase):

    def test_find(self):

        self.assertEqual(5, find_second_max([5, 4, 3, 2, 5]))
        self.assertEqual(5, find_second_max([5, 5, 4, 3, 2]))
        self.assertEqual(4, find_second_max([2, 3, 5, 4]))
        self.assertEqual(90, find_second_max([1, 3, -2, 100, 90, 10]))
        self.assertEqual(-3, find_second_max([-100, -3, 0, -90]))
