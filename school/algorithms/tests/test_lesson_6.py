from unittest import TestCase

from algorithms.lesson_6 import Deque


class TestLesson6(TestCase):

    def setUp(self) -> None:

        self.d = Deque()
        self.d.addFront(1)
        self.d.addFront(1)
        self.d.addTail(2)
        self.d.addTail(2)
        self.d.addTail(3)
        self.d.addTail(3)

        self.empty_d = Deque()

    def test_get_values(self) -> None:

        expected_values = [1, 1, 2, 2, 3, 3]
        self.assertEqual(expected_values, self.d.get_values())
        self.assertEqual([], self.empty_d.get_values())

    def test_add_front(self) -> None:

        expected_values = [-100, 999, 1, 1, 2, 2, 3, 3]
        self.d.addFront(999)
        self.assertEqual(7, self.d.size())
        self.d.addFront(-100)
        self.assertEqual(8, self.d.size())
        self.assertEqual(expected_values, self.d.get_values())

        expected_values = [1000, 100500]
        self.empty_d.addFront(100500)
        self.assertEqual(1, self.empty_d.size())
        self.empty_d.addFront(1000)
        self.assertEqual(2, self.empty_d.size())
        self.assertEqual(expected_values, self.empty_d.get_values())

    def test_add_tail(self) -> None:

        expected_values = [1, 1, 2, 2, 3, 3, 999, -100]
        self.d.addTail(999)
        self.assertEqual(7, self.d.size())
        self.d.addTail(-100)
        self.assertEqual(8, self.d.size())
        self.assertEqual(expected_values, self.d.get_values())

        expected_values = [100500, 1000]
        self.empty_d.addTail(100500)
        self.assertEqual(1, self.empty_d.size())
        self.empty_d.addTail(1000)
        self.assertEqual(2, self.empty_d.size())
        self.assertEqual(expected_values, self.empty_d.get_values())

    def test_remove_front(self) -> None:

        expected_values = [2, 3, 3]
        self.assertEqual(1, self.d.removeFront())
        self.assertEqual(5, self.d.size())

        self.assertEqual(1, self.d.removeFront())
        self.assertEqual(4, self.d.size())

        self.assertEqual(2, self.d.removeFront())
        self.assertEqual(3, self.d.size())

        self.assertEqual(expected_values, self.d.get_values())

        self.assertEqual(2, self.d.removeFront())
        self.assertEqual(2, self.d.size())

        self.assertEqual(3, self.d.removeFront())
        self.assertEqual(1, self.d.size())

        self.assertEqual(3, self.d.removeFront())
        self.assertEqual(0, self.d.size())

        self.assertEqual(None, self.d.removeFront())
        self.assertEqual(0, self.d.size())
        self.assertEqual(None, self.d.removeFront())
        self.assertEqual(0, self.d.size())

        self.assertEqual(None, self.empty_d.removeFront())
        self.assertEqual(None, self.empty_d.removeFront())
        self.empty_d.addFront(100)
        self.empty_d.addFront(200)
        self.assertEqual(200, self.empty_d.removeFront())
        self.assertEqual(100, self.empty_d.removeFront())
        self.assertEqual(None, self.empty_d.removeFront())

    def test_remove_tail(self) -> None:

        expected_values = [1, 1, 2]
        self.assertEqual(3, self.d.removeTail())
        self.assertEqual(5, self.d.size())

        self.assertEqual(3, self.d.removeTail())
        self.assertEqual(4, self.d.size())

        self.assertEqual(2, self.d.removeTail())
        self.assertEqual(3, self.d.size())

        self.assertEqual(expected_values, self.d.get_values())

        self.assertEqual(2, self.d.removeTail())
        self.assertEqual(2, self.d.size())

        self.assertEqual(1, self.d.removeTail())
        self.assertEqual(1, self.d.size())

        self.assertEqual(1, self.d.removeTail())
        self.assertEqual(0, self.d.size())

        self.assertEqual(None, self.d.removeTail())
        self.assertEqual(0, self.d.size())

        self.assertEqual(None, self.d.removeTail())
        self.assertEqual(0, self.d.size())

        self.assertEqual(None, self.empty_d.removeTail())
        self.assertEqual(None, self.empty_d.removeTail())
        self.empty_d.addTail(100)
        self.empty_d.addTail(200)
        self.assertEqual(200, self.empty_d.removeTail())
        self.assertEqual(100, self.empty_d.removeTail())
        self.assertEqual(None, self.empty_d.removeTail())

    def test_add_remove(self) -> None:

        expected_values = [2, 2, 3, 3, 1, 1]
        self.d.addTail(self.d.removeFront())
        self.d.addTail(self.d.removeFront())
        self.assertEqual(expected_values, self.d.get_values())

        expected_values = [1, 1, 2, 2, 3, 3]
        self.d.addFront(self.d.removeTail())
        self.d.addFront(self.d.removeTail())
        self.assertEqual(expected_values, self.d.get_values())

    def test_stress(self) -> None:

        for i in range(10000):
            self.d.addFront(i)
            self.assertEqual((7 + i), self.d.size())
        for i in range(10000):
            self.d.addTail(self.d.removeFront())
            self.assertEqual(10006, self.d.size())
