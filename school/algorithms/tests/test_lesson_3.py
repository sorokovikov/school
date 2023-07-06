from unittest import TestCase

from algorithms.lesson_3 import DynArray


class TestLessonThree(TestCase):

    def setUp(self) -> None:

        self.da = DynArray()
        self.da.append(1)
        self.da.append(2)
        self.da.append(4)
        self.da.append(1)
        self.da.append(9)

        self.big_da = DynArray()
        for i in range(34):
            self.big_da.append(i)

        self.empty_da = DynArray()

    def test_insert_buffer_same(self):

        expected_values = [1, 999, 2, 4, 222, 1, 9]

        self.da.insert(1, 999)
        self.da.insert(4, 222)
        self.assertEqual(expected_values, self.da.get_values())
        self.assertEqual(16, self.da.capacity)

    def test_insert_in_tail(self):

        expected_values = [1, 2, 4, 1, 9, 999, 222]
        self.da.insert(5, 999)
        self.da.insert(6, 222)
        self.assertEqual(expected_values, self.da.get_values())
        self.assertEqual(16, self.da.capacity)

        expected_values = [999, -100]
        self.empty_da.insert(0, 999)
        self.empty_da.insert(1, -100)
        self.assertEqual(expected_values, self.empty_da.get_values())

    def test_insert_in_start(self):

        expected_value = [-100, 999, 1, 2, 4, 1, 9]
        self.da.insert(0, 999)
        self.da.insert(0, -100)
        self.assertEqual(expected_value, self.da.get_values())
        self.assertEqual(7, self.da.count)

        expected_value = [-100, 999]
        self.empty_da.insert(0, 999)
        self.empty_da.insert(0, -100)
        self.assertEqual(expected_value, self.empty_da.get_values())
        self.assertEqual(2, self.empty_da.count)

    def test_insert_buffer_increase(self):

        expected_values = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 1, 2, 4, 1, 9]

        for _ in range(12):
            self.da.insert(0, 999)
        self.assertEqual(expected_values, self.da.get_values())
        self.assertEqual(32, self.da.capacity)

    def test_insert_raise_error(self):

        self.assertRaises(IndexError, lambda: self.da.insert(100, 999))
        self.assertRaises(IndexError, lambda: self.da.insert(-1, 999))

    def test_delete_buffer_same(self):

        expected_values = [0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
        self.big_da.delete(2)
        self.big_da.delete(1)
        self.assertEqual(expected_values, self.big_da.get_values())
        self.assertEqual(64, self.big_da.capacity)
        self.assertEqual(32, self.big_da.count)

    def test_delete_buffer_decrease(self):

        expected_values = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
        self.big_da.delete(2)
        self.big_da.delete(1)
        self.big_da.delete(0)
        self.assertEqual(expected_values, self.big_da.get_values())
        self.assertEqual(42, self.big_da.capacity)
        self.assertEqual(31, self.big_da.count)

    def test_delete_until_minimum_buffer(self):

        for _ in range(30):
            self.big_da.delete(0)
        self.assertEqual(16, self.big_da.capacity)
        print(self.big_da.get_values())

    def test_delete_raise_error(self):

        self.assertRaises(IndexError, lambda: self.empty_da.delete(0))

        self.assertRaises(IndexError, lambda: self.big_da.delete(999))
        self.assertRaises(IndexError, lambda: self.big_da.delete(-1))
