from unittest import TestCase

from algorithms.lesson_8 import HashTable


class TestHashTable(TestCase):

    def setUp(self) -> None:

        self.h = HashTable(19, 3)
        self.h.put("hello")
        self.h.put("world")

        self.big_h = HashTable(10000, 5)

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
        self.assertEqual(12, self.h.put("hello2"))

        for i in range(10000, 30400):
            self.h.put(f"foo bar foo bar {i}")
            self.big_h.put(f"foo bar foo bar {i}")

        for i in range(self.h.size):
            print(self.h.slots[i])

        for i in range(self.h.size):
            self.assertIsNotNone(self.h.slots[i])

        for i in range(self.big_h.size):
            self.assertIsNotNone(self.big_h.slots[i])

    def test_find(self) -> None:

        self.h.put("world2")
        self.h.put("hello2")

        self.assertEqual(0, self.h.find("hello"))
        self.assertEqual(1, self.h.find("world"))
        self.assertEqual(13, self.h.find("world2"))
        self.assertEqual(12, self.h.find("hello2"))
        self.assertIsNone(self.h.find("world3"))
        self.assertIsNone(self.h.find("hello3"))
