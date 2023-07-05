from unittest import TestCase

from algorithms.lesson_3 import DynArray


class TestLessonThree(TestCase):

    def setUp(self) -> None:

        self.d = DynArray()
        self.d.append(1)
        self.d.append(2)
        self.d.append(4)
        self.d.append(1)
        self.d.append(9)

    def test_insert_buffer_same(self):

        expected_values = [1, 999, 2, 4, 222, 1, 9]

        self.d.insert(1, 999)
        self.d.insert(4, 222)
        self.assertEqual(expected_values, self.d.get_values())
        self.assertEqual(16, self.d.capacity)

    def test_insert_buffer_increase(self):

        expected_values = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 1, 2, 4, 1, 9]

        for _ in range(12):
            self.d.insert(0, 999)
        self.assertEqual(expected_values, self.d.get_values())
        self.assertEqual(32, self.d.capacity)
