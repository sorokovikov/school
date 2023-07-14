from unittest import TestCase

from algorithms.lesson_4_additional import (
    check_parentheses,
    convert_postfix_notation_to_stack,
    calculate_postfix_notation,
    StackHead,
)


class TestLesson4StackHead(TestCase):

    def setUp(self) -> None:

        self.s = StackHead()
        self.s.push(1)
        self.s.push(1)
        self.s.push(2)
        self.s.push(2)
        self.s.push(3)
        self.s.push(3)

        self.empty_s = StackHead()

    def test_stack_values_sequence(self):

        self.assertEqual([3, 3, 2, 2, 1, 1], self.s.get_values())

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

        expected_values = [-100, 999, 3, 3, 2, 2, 1, 1]
        self.s.push(999)
        self.s.push(-100)
        self.assertEqual(expected_values, self.s.get_values())

        expected_values = [400, 555]
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


class TestLesson4Additional(TestCase):

    def test_check_parentheses_true(self):

        self.assertTrue(check_parentheses("((()))"))
        self.assertTrue(check_parentheses("(()((())()))"))
        self.assertTrue(check_parentheses("()()()()()()"))
        self.assertTrue(check_parentheses("((()()))()(())"))

    def test_check_parentheses_false(self):

        self.assertFalse(check_parentheses("))(("))
        self.assertFalse(check_parentheses("())"))
        self.assertFalse(check_parentheses("(()"))
        self.assertFalse(check_parentheses("())("))
        self.assertFalse(check_parentheses("(((((()))))"))
        self.assertFalse(check_parentheses("(()((()())())()("))
        self.assertFalse(check_parentheses("()((())"))

    def test_postfix_notation(self):

        s = convert_postfix_notation_to_stack("8 2 + 5 * 9 + =")
        self.assertEqual(59, calculate_postfix_notation(s))

        s = convert_postfix_notation_to_stack("99 -1 * 100 + =")
        self.assertEqual(1, calculate_postfix_notation(s))

        s = convert_postfix_notation_to_stack("100500 100500 + 2 * =")
        self.assertEqual(402000, calculate_postfix_notation(s))
