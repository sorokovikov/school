from unittest import TestCase

from algorithms.lesson_4_additional import check_parentheses


class TestLesson4Additional(TestCase):

    def test_true(self):

        self.assertTrue(check_parentheses("((()))"))
        self.assertTrue(check_parentheses("(()((())()))"))
        self.assertTrue(check_parentheses("()()()()()()"))
        self.assertTrue(check_parentheses("((()()))()(())"))

    def test_false(self):

        self.assertFalse(check_parentheses("))(("))
        self.assertFalse(check_parentheses("())"))
        self.assertFalse(check_parentheses("(()"))
        self.assertFalse(check_parentheses("())("))
        self.assertFalse(check_parentheses("(((((()))))"))
        self.assertFalse(check_parentheses("()((())"))
