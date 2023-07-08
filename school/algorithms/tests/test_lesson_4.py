from unittest import TestCase

from algorithms.lesson_4 import Stack


class TestLesson4(TestCase):

    def setUp(self) -> None:

        self.s = Stack()
        self.s.push(1)
        self.s.push(1)
        self.s.push(2)
        self.s.push(2)
        self.s.push(3)
        self.s.push(3)

        self.empty_s = Stack()

    def test_size(self) -> None:

        self.assertEqual(6, self.s.size())
        self.assertEqual(0, self.empty_s.size())

        self.s.push(100)
        self.empty_s.push(999)
        self.assertEqual(7, self.s.size())
        self.assertEqual(1, self.empty_s.size())

        self.s.pop()
        self.s.pop()
        self.assertEqual(5, self.s.size())

    def test_push(self) -> None:

        expected_values = [1, 1, 2, 2, 3, 3, 999, -100]
        self.s.push(999)
        self.s.push(-100)
        self.assertEqual(expected_values, self.s.get_values())

        expected_values = [555, 400]
        self.empty_s.push(555)
        self.empty_s.push(400)
        self.assertEqual(expected_values, self.empty_s.get_values())

    def test_pop(self) -> None:

        self.assertEqual(3, self.s.pop())
        self.assertEqual(3, self.s.pop())
        self.assertEqual(2, self.s.pop())
        self.assertEqual(2, self.s.pop())
        self.assertEqual(1, self.s.pop())
        self.assertEqual(1, self.s.pop())
        self.assertEqual(None, self.s.pop())
        self.assertEqual(None, self.s.pop())

        self.assertEqual(None, self.empty_s.pop())

        self.s.push(999)
        self.assertEqual(999, self.s.pop())

    def test_peek(self):

        self.assertEqual(3, self.s.peek())
        self.assertEqual(3, self.s.peek())
        self.assertEqual(3, self.s.peek())
        self.assertEqual(None, self.empty_s.peek())
        self.assertEqual(None, self.empty_s.peek())
        self.assertEqual(None, self.empty_s.peek())

        self.s.pop()  # 3
        self.s.pop()  # 2
        self.s.pop()  # 2
        self.assertEqual(2, self.s.peek())
        self.s.pop()  # 1
        self.assertEqual(1, self.s.peek())
        self.s.pop()  # 1
        self.assertEqual(1, self.s.peek())
        self.s.pop()  # None
        self.assertEqual(None, self.s.peek())
