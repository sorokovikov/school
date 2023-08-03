from unittest import TestCase

from algorithms.lesson_8 import HashTable


class TestHashTable(TestCase):

    def setUp(self) -> None:

        self.h = HashTable(19, 3)
        self.h.put("hello")
        self.h.put("world")

    def test_hash(self) -> None:

        self.assertEqual(0, self.h.hash_fun("hello"))
        self.assertEqual(1, self.h.hash_fun("world"))

    def test_seek_slot(self) -> None:

        self.assertEqual(13, self.h.seek_slot("world2"))
        self.assertEqual(13, self.h.seek_slot("world2"))
        self.assertEqual(12, self.h.seek_slot("hello2"))
        self.assertEqual(12, self.h.seek_slot("hello2"))

    def test_put(self) -> None:

        self.assertEqual(13, self.h.put("world2"))
        self.assertEqual(13, self.h.put("world2"))
        self.assertEqual(12, self.h.put("world2"))
