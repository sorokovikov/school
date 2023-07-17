from unittest import TestCase

from algorithms.lesson_6_additional import is_palindrome


class TestIsPalindrome(TestCase):

    def test_true(self) -> None:

        self.assertTrue(is_palindrome("qwertyytrewq"))
        self.assertTrue(is_palindrome("12345678900987654321"))
        self.assertFalse(is_palindrome("aaaa"))

        self.assertTrue(is_palindrome("civic"))
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("deified"))

    def test_false(self) -> None:

        self.assertFalse(is_palindrome("qwertyutrewq"))
        self.assertFalse(is_palindrome("hello world"))
        self.assertFalse(is_palindrome("1234567897654321"))
        self.assertFalse(is_palindrome("aaaab"))
        self.assertFalse(is_palindrome("  world"))
