from unittest import TestCase

from algorithms.lesson_5 import Queue


class TestLesson5(TestCase):

    def setUp(self) -> None:

        self.q = Queue()
        self.q.enqueue(1)
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(2)
        self.q.enqueue(3)
        self.q.enqueue(3)

        self.empty_q = Queue()

    def test_get_values(self):

        expected_values = [1, 1, 2, 2, 3, 3]
        self.assertEqual(expected_values, self.q.get_values())
        self.assertEqual([], self.empty_q.get_values())

    def test_enqueue(self):

        self.q.enqueue(999)
        self.q.enqueue(-100)

        expected_values = [1, 1, 2, 2, 3, 3, 999, -100]
        self.assertEqual(expected_values, self.q.get_values())

        expected_values = [-1, 200]
        self.empty_q.enqueue(-1)
        self.empty_q.enqueue(200)
        self.assertEqual(expected_values, self.empty_q.get_values())

    def test_dequeue(self):

        self.assertEqual(1, self.q.dequeue())
        self.assertEqual(1, self.q.dequeue())
        self.assertEqual(2, self.q.dequeue())
        self.assertEqual(2, self.q.dequeue())
        self.assertEqual(3, self.q.dequeue())
        self.assertEqual(3, self.q.dequeue())
        self.assertEqual(None, self.q.dequeue())
        self.assertEqual(None, self.q.dequeue())

        self.assertEqual(None, self.empty_q.dequeue())

        self.q.enqueue(100500)
        self.assertEqual(100500, self.q.dequeue())

    def test_size(self):

        self.assertEqual(6, self.q.size())
        self.assertEqual(0, self.empty_q.size())

        self.q.dequeue()
        self.q.dequeue()
        self.assertEqual(4, self.q.size())

        self.empty_q.dequeue()
        self.assertEqual(0, self.empty_q.size())

        self.q.enqueue(100)
        self.assertEqual(5, self.q.size())

        self.empty_q.enqueue(100)
        self.assertEqual(1, self.empty_q.size())
