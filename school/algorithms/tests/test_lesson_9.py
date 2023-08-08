from unittest import TestCase

from algorithms.lesson_9 import NativeDictionary


class TestLesson9(TestCase):

    def setUp(self) -> None:

        self.n = NativeDictionary(20)
        self.n.put("foo", 100)
        self.n.put("bar", 100)

        self.big_n = NativeDictionary(10000)

    def test_is_key(self) -> None:

        self.assertTrue(self.n.is_key("foo"))
        self.assertTrue(self.n.is_key("bar"))

        self.assertFalse(self.n.is_key("hello"))
        self.assertFalse(self.n.is_key("world"))

    def test_get(self) -> None:

        self.assertEqual(100, self.n.get("foo"))
        self.assertEqual(100, self.n.get("bar"))

        self.assertEqual(None, self.n.get("hello"))
        self.assertEqual(None, self.n.get("world"))

    def test_put(self) -> None:

        self.assertTrue(self.n.is_key("foo"))
        self.assertEqual(100, self.n.get("foo"))
        self.assertTrue(self.n.is_key("bar"))
        self.assertEqual(100, self.n.get("bar"))

        self.n.put("bar", 999)
        self.assertTrue(self.n.is_key("bar"))
        self.assertEqual(999, self.n.get("bar"))

        self.n.put("hello", 100500)
        self.assertTrue(self.n.is_key("hello"))
        self.assertEqual(100500, self.n.get("hello"))

        self.n.put("hello", -1)
        self.assertTrue(self.n.is_key("hello"))
        self.assertEqual(-1, self.n.get("hello"))

    def test_stress(self) -> None:

        for i in range(10000):
            self.big_n.put(f"foo bar {i}", i)
