from unittest import TestCase

from atd_1.lesson_1_stack import BoundedStack


class TestLesson1(TestCase):

    def setUp(self):

        self.stack = BoundedStack()

    def test_init(self):

        self.assertEqual(0, self.stack.size())
        self.assertEqual(BoundedStack.PEAK_NIL, self.stack.get_peak_status())
        self.assertEqual(BoundedStack.POP_NIL, self.stack.get_pop_status())
        self.assertEqual(BoundedStack.PUSH_NIL, self.stack.get_push_status())

    def test_size(self):

        self.assertEqual(0, self.stack.size())

        with self.subTest():
            for i in range(1, 5):
                self.stack.push(1)
                self.assertEqual(i, self.stack.size())

            for i in range(3, -1, -1):
                self.stack.pop()
                self.assertEqual(i, self.stack.size())

    def test_push(self):

        self.stack.push(1)

        self.assertEqual(1, self.stack.size())
        self.assertEqual(BoundedStack.PUSH_OK, self.stack.get_push_status())
        self.assertEqual(1, self.stack.peak())

    def test_default_max_size(self):

        for _ in range(32):
            self.stack.push(1337)

        self.assertEqual(32, self.stack.size())
        self.assertEqual(BoundedStack.PUSH_OK, self.stack.get_push_status())
        self.assertEqual(1337, self.stack.peak())

        self.stack.push(1)

        self.assertEqual(BoundedStack.PUSH_ERR, self.stack.get_push_status())
        self.assertEqual(32, self.stack.size())
        self.assertEqual(1337, self.stack.peak())

    def test_max_size(self):

        stack = BoundedStack(5)

        for _ in range(5):
            stack.push(227)

        self.assertEqual(5, stack.size())
        self.assertEqual(BoundedStack.PUSH_OK, stack.get_push_status())
        self.assertEqual(227, stack.peak())

        stack.push(228)

        self.assertEqual(BoundedStack.PUSH_ERR, stack.get_push_status())
        self.assertEqual(5, stack.size())
        self.assertEqual(227, stack.peak())

    def test_pop(self):

        self.stack.push(10)
        self.stack.push(20)

        self.stack.pop()

        self.assertEqual(BoundedStack.POP_OK, self.stack.get_pop_status())
        self.assertEqual(10, self.stack.peak())

        self.stack.pop()
        self.stack.pop()

        self.assertEqual(BoundedStack.POP_ERR, self.stack.get_pop_status())

    def test_clear(self):

        for _ in range(32):
            self.stack.push(10)

        self.assertEqual(32, self.stack.size())

        self.stack.clear()

        self.assertEqual(0, self.stack.size())
        self.assertEqual(BoundedStack.PEAK_NIL, self.stack.get_peak_status())
        self.assertEqual(BoundedStack.POP_NIL, self.stack.get_pop_status())
        self.assertEqual(BoundedStack.PUSH_NIL, self.stack.get_push_status())

    def test_peak(self):

        for i in range(10):
            self.stack.push(i)
            self.assertEqual(i, self.stack.peak())
