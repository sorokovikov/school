from unittest import TestCase

from algorithms.lesson_11 import BloomFilter


class TestLesson11(TestCase):

    def setUp(self) -> None:

        self.bf = BloomFilter(32)
        self.bf.add("0123456789")

    def test_is_value(self) -> None:

        self.assertTrue(self.bf.is_value("0123456789"))
        self.assertFalse(self.bf.is_value("9012345678"))
        self.assertFalse(self.bf.is_value("7890123456"))
        self.assertFalse(self.bf.is_value("5678901234"))
        self.assertFalse(self.bf.is_value("3456789012"))
        self.assertFalse(self.bf.is_value("1234567890"))

    def test_add(self) -> None:

        self.bf.add("2345678901")
        self.assertTrue(self.bf.is_value("2345678901"))

        self.bf.add("1234567890")
        self.assertTrue(self.bf.is_value("1234567890"))

        self.bf.add("9012345678")
        self.assertTrue(self.bf.is_value("9012345678"))

        self.bf.add("8901234567")
        self.assertTrue(self.bf.is_value("8901234567"))

        self.bf.add("7890123456")
        self.assertTrue(self.bf.is_value("7890123456"))

        self.bf.add("6789012345")
        self.assertTrue(self.bf.is_value("6789012345"))

        self.bf.add("5678901234")
        self.assertTrue(self.bf.is_value("5678901234"))

        self.bf.add("4567890123")
        self.assertTrue(self.bf.is_value("4567890123"))

        self.bf.add("3456789012")
        self.assertTrue(self.bf.is_value("3456789012"))

        self.bf.add("2345678901")
        self.assertTrue(self.bf.is_value("2345678901"))

        self.bf.add("1234567890")
        self.assertTrue(self.bf.is_value("1234567890"))

