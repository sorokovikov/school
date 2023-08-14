from unittest import TestCase

from algorithms.lesson_10 import PowerSet


class TestLesson10(TestCase):

    def setUp(self) -> None:

        self.ps = PowerSet()
        self.ps.put(1)
        self.ps.put(2)
        self.ps.put(3)
        self.ps.put(4)
        self.ps.put(5)
        self.ps.put(6)

        self.big_ps = PowerSet()
        for i in range(20000):
            self.big_ps.put(i)
        self.big_ps2 = PowerSet()
        for i in range(10000, 30000):
            self.big_ps2.put(i)

    def test_put(self) -> None:

        self.ps.put(7)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], self.ps.storage)
        self.assertEqual(7, self.ps.size())
        self.assertTrue(self.ps.get(7))
        self.ps.put(7)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], self.ps.storage)
        self.assertEqual(7, self.ps.size())
        self.assertTrue(self.ps.get(7))
        self.ps.put(8)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], self.ps.storage)
        self.assertEqual(8, self.ps.size())
        self.assertTrue(self.ps.get(8))
        self.ps.put(8)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], self.ps.storage)
        self.assertEqual(8, self.ps.size())
        self.assertTrue(self.ps.get(8))

    def test_remove(self) -> None:

        self.ps.remove(5)
        self.assertEqual([1, 2, 3, 4, 6], self.ps.storage)
        self.assertEqual(5, self.ps.size())
        self.assertFalse(self.ps.get(5))
        self.ps.remove(5)
        self.assertEqual([1, 2, 3, 4, 6], self.ps.storage)
        self.assertEqual(5, self.ps.size())
        self.assertFalse(self.ps.get(5))
        self.ps.remove(1)
        self.assertEqual([2, 3, 4, 6], self.ps.storage)
        self.assertEqual(4, self.ps.size())
        self.assertFalse(self.ps.get(1))

    def test_intersection(self) -> None:

        ps2 = PowerSet()
        ps2.put(1)
        ps2.put(2)
        ps2.put(6)
        ps2.put(7)
        ps2.put(9)
        self.assertEqual([1, 2, 6], self.ps.intersection(ps2).storage)
        ps2.put(100)
        self.assertEqual([1, 2, 6], self.ps.intersection(ps2).storage)
        ps2.put(4)
        self.assertEqual([1, 2, 4, 6], self.ps.intersection(ps2).storage)

        ps3 = PowerSet()
        ps3.put(100)
        ps3.put(200)
        ps3.put(300)
        self.assertEqual([], self.ps.intersection(ps3).storage)

        self.assertEqual([], self.ps.intersection(PowerSet()).storage)

    def test_union(self) -> None:

        ps2 = PowerSet()
        ps2.put(1)
        ps2.put(4)
        ps2.put(100)
        ps2.put(6)
        ps2.put(200)
        ps2.put(300)
        ps2.put(5)
        self.assertEqual([1, 2, 3, 4, 5, 6, 100, 200, 300], self.ps.union(ps2).storage)
        ps2.put(500)
        ps2.put(2)
        self.assertEqual([1, 2, 3, 4, 5, 6, 100, 200, 300, 500], self.ps.union(ps2).storage)

        self.assertEqual([1, 2, 3, 4, 5, 6], self.ps.union(PowerSet()).storage)

    def test_difference(self) -> None:

        ps2 = PowerSet()
        ps2.put(1)
        ps2.put(6)
        ps2.put(100)
        ps2.put(200)
        ps2.put(300)
        self.assertEqual([2, 3, 4, 5], self.ps.difference(ps2).storage)

        ps3 = PowerSet()
        ps3.put(1)
        ps3.put(2)
        ps3.put(3)
        ps3.put(4)
        ps3.put(5)
        ps3.put(6)
        self.assertEqual([], self.ps.difference(ps3).storage)

        ps3.put(7)
        ps3.put(8)
        self.assertEqual([], self.ps.difference(ps3).storage)

    def test_issubset(self) -> None:

        ps2 = PowerSet()
        ps2.put(1)
        ps2.put(2)
        ps2.put(3)
        self.assertTrue(self.ps.issubset(ps2))
        ps2.put(4)
        self.assertTrue(self.ps.issubset(ps2))
        ps2.put(100)
        self.assertFalse(self.ps.issubset(ps2))

    def test_stress(self) -> None:

        self.assertEqual([i for i in range(10000, 20000)], self.big_ps.intersection(self.big_ps2).storage)
        self.assertEqual([i for i in range(30000)], self.big_ps.union(self.big_ps2).storage)
        self.assertEqual([i for i in range(10000)], self.big_ps.difference(self.big_ps2).storage)
