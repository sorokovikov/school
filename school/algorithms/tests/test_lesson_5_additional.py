from unittest import TestCase

from algorithms.lesson_5 import Queue
from algorithms.lesson_5_additional import rotate_queue, QueueWithStacks


class TestLesson5QueueWithTwoStacks(TestCase):

    def setUp(self) -> None:

        self.q = QueueWithStacks()
        self.q.enqueue(1)
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(2)
        self.q.enqueue(3)
        self.q.enqueue(3)

        self.empty_q = QueueWithStacks()

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

        self.q.dequeue()
        self.q.dequeue()
        self.q.dequeue()
        self.q.dequeue()
        self.q.dequeue()
        self.q.dequeue()
        self.assertEqual(0, self.q.size())

        self.empty_q.enqueue(100)
        self.assertEqual(1, self.empty_q.size())

    def test_stress(self):

        for i in range(10000):
            self.q.enqueue(i)

        for i in range(10000):
            self.q.enqueue(self.q.dequeue())


class TestLesson5Rotation(TestCase):

    def setUp(self) -> None:

        self.q = QueueWithStacks()
        self.q.enqueue(1)
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(2)
        self.q.enqueue(3)
        self.q.enqueue(3)

        self.big_q = QueueWithStacks()
        for i in range(10000):
            self.big_q.enqueue(i)

    def test_rotate(self) -> None:

        expected_values = [2, 2, 3, 3, 1, 1]
        rotate_queue(self.q, 2)
        self.assertEqual(expected_values, self.q.get_values())

        expected_values = [i for i in range(100, 10000)]
        expected_values.extend([i for i in range(100)])
        rotate_queue(self.big_q, 100)
        self.assertEqual(expected_values, self.big_q.get_values())
