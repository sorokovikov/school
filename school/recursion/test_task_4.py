from unittest import TestCase

from recursion.task_4 import is_palindrome


class TestIsPalindrome(TestCase):

    def test_is_palindrome(self):

        self.assertTrue(is_palindrome("foooof"))
        self.assertTrue(is_palindrome("bab"))
        self.assertTrue(is_palindrome("ПриветтевирП"))
        self.assertTrue(is_palindrome("ПриветевирП"))
        self.assertTrue(is_palindrome("aa"))

        self.assertFalse(is_palindrome("fooooob"))
        self.assertFalse(is_palindrome("HelloalleH"))
        self.assertFalse(is_palindrome("BOO"))
        self.assertFalse(is_palindrome("BO"))
