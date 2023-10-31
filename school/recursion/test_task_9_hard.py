from unittest import TestCase

from algorithms.lesson_4_additional import check_parentheses
from recursion.task_9_hard import generate_balanced_parentheses_list


class TestGenerator(TestCase):

    def test_generator(self) -> None:

        parentheses_list = generate_balanced_parentheses_list(3)

        for parentheses in parentheses_list:
            with self.subTest():
                self.assertTrue(check_parentheses(parentheses))

        parentheses_list = generate_balanced_parentheses_list(5)

        for parentheses in parentheses_list:
            with self.subTest():
                self.assertTrue(check_parentheses(parentheses))
