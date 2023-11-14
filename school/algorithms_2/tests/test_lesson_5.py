from unittest import TestCase

from algorithms_2.lesson_5 import GenerateBBSTArray


class TestLesson5(TestCase):

    def test_generate_bbst_array(self):

        self.assertEqual([], GenerateBBSTArray([]))
        self.assertEqual([4, 2, 6, 1, 3, 5, 7], GenerateBBSTArray([7, 6, 5, 4, 3, 2, 1]))
        self.assertEqual(
            [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15],
            GenerateBBSTArray([7, 6, 5, 4, 3, 2, 1, 15, 14, 13, 12, 11, 10, 9, 8]),
        )
