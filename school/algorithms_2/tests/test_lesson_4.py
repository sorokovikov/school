from unittest import TestCase

from algorithms_2.lesson_4 import aBST


class TestLesson4(TestCase):

    def setUp(self):

        self.t = aBST(2)

        self.t.AddKey(50)
        self.t.AddKey(35)
        self.t.AddKey(75)

    def test_len(self):

        self.assertEqual(7, len(self.t.Tree))

    def test_add_key(self):

        self.assertEqual(3, self.t.AddKey(25))
        self.assertEqual(3, self.t.AddKey(25))
        self.assertEqual(6, self.t.AddKey(80))
        self.assertEqual(5, self.t.AddKey(60))
        self.assertEqual(4, self.t.AddKey(40))
        self.assertEqual(-1, self.t.AddKey(100))

    def test_find_key_index(self):

        self.assertEqual(0, self.t.FindKeyIndex(50))
        self.assertEqual(1, self.t.FindKeyIndex(35))
        self.assertEqual(2, self.t.FindKeyIndex(75))
        self.assertEqual(-3, self.t.FindKeyIndex(25))
        self.assertEqual(-6, self.t.FindKeyIndex(80))
        self.assertEqual(-5, self.t.FindKeyIndex(60))
        self.assertEqual(-4, self.t.FindKeyIndex(40))

        self.t.AddKey(25)
        self.t.AddKey(25)
        self.t.AddKey(80)
        self.t.AddKey(60)
        self.t.AddKey(40)

        self.assertIsNone(self.t.FindKeyIndex(100))
