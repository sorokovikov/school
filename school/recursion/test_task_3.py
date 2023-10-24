from unittest import TestCase

from recursion.task_3 import list_length


class TestListLength(TestCase):

    def test_list_length(self):

        self.assertEqual(10, list_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        self.assertEqual(0, list_length([]))
        self.assertEqual(200, list_length([i for i in range(200)]))
