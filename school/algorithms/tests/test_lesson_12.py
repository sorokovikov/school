from unittest import TestCase

from algorithms.lesson_12 import NativeCache


class TestLesson12(TestCase):

    def setUp(self) -> None:

        self.cache = NativeCache(5)
        self.cache.put("foo", 100)
        self.cache.put("bar", 200)

    def test_hits(self) -> None:

        foo_index = self.cache.seek_slot("foo")
        self.assertEqual(0, self.cache.hits[foo_index])

        self.cache.get("foo")
        self.cache.get("foo")
        self.assertEqual(2, self.cache.hits[foo_index])

        self.cache.get("foo")
        self.cache.get("foo")
        self.cache.get("foo")
        self.cache.get("foo")
        self.assertEqual(6, self.cache.hits[foo_index])

    def test_exclude(self) -> None:

        self.cache.get("foo")
        self.cache.get("foo")
        self.cache.get("foo")
        self.cache.get("foo")
        self.cache.get("foo")

        self.cache.get("bar")
        self.cache.get("bar")
        self.cache.get("bar")
        self.cache.get("bar")
        self.cache.get("bar")

        for i in range(1, 3):
            self.cache.put(f"Index {i}", i)
            for j in range(i):
                self.cache.get(f"Index {i}")

        index1 = self.cache.seek_slot("Index 1")
        self.assertEqual("Index 1", self.cache.slots[index1])
        self.assertEqual(1, self.cache.values[index1])
        self.assertEqual(1, self.cache.hits[index1])

        index2 = self.cache.seek_slot("Index 2")
        self.assertEqual("Index 2", self.cache.slots[index2])
        self.assertEqual(2, self.cache.values[index2])
        self.assertEqual(2, self.cache.hits[index2])

        self.cache.put("Index 3", 3)
        self.cache.get("Index 3")
        self.cache.get("Index 3")
        self.cache.get("Index 3")

        self.assertTrue(self.cache.is_key("Index 1"))
        self.cache.put("Index 4", 4)
        self.assertFalse(self.cache.is_key("Index 1"))

        self.cache.get("Index 4")
        self.cache.get("Index 4")
        self.cache.get("Index 4")
        self.cache.get("Index 4")

        self.assertTrue(self.cache.is_key("Index 2"))
        self.cache.put("Index 5", 5)
        self.assertFalse(self.cache.is_key("Index 2"))

        self.assertTrue(self.cache.is_key("Index 5"))
        self.cache.put("Index 6", 6)
        self.assertFalse(self.cache.is_key("Index 5"))

        self.cache.put("Index 6", 100)
        self.assertTrue(self.cache.is_key("Index 6"))
