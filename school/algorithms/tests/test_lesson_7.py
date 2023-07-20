from unittest import TestCase

from algorithms.lesson_7 import OrderedList, OrderedStringList, Node


class TestOrderedList(TestCase):

    def setUp(self) -> None:

        self.ol = OrderedList(True)
        self.ol.add(999)
        self.ol.add(100)
        self.ol.add(500)
        self.ol.add(345)
        self.ol.add(100000)
        self.ol.add(1)

    def test_len(self) -> None:

        self.assertEqual(6, self.ol.len())
        self.ol.add(10)
        self.ol.add(10)
        self.ol.add(10)
        self.assertEqual(9, self.ol.len())

    def test_get_values(self) -> None:

        self.assertEqual([1, 100, 345, 500, 999, 100000], self.ol.get_nodes_values())
        self.assertEqual(1, self.ol.head.value)
        self.assertEqual(100000, self.ol.tail.value)

        self.ol.add(99999)
        self.assertEqual([1, 100, 345, 500, 999, 99999, 100000], self.ol.get_nodes_values())

    def test_find(self) -> None:

        self.assertIsNone(self.ol.find(100500))
        self.assertIsNone(self.ol.find(99))
        self.assertIsNotNone(self.ol.find(999))
        self.assertIsNotNone(self.ol.find(1))

        self.ol.add(100500)
        self.assertIsNotNone(self.ol.find(100500))

    def test_delete(self) -> None:

        self.ol.delete(999)
        self.assertIsNone(self.ol.find(999))

    def test_add(self) -> None:

        self.ol.add(45678)
        self.ol.add(987)
        self.ol.add(1485)
        self.ol.add(1855)
        self.ol.add(421)
        self.ol.add(-97512)
        self.ol.add(-479)
        self.ol.add(-95)
        self.ol.add(95761)
        self.ol.add(5012366)
        self.assertEqual(
            [
                -97512,
                -479,
                -95,
                1,
                100,
                345,
                421,
                500,
                987,
                999,
                1485,
                1855,
                45678,
                95761,
                100000,
                5012366,
            ],
            self.ol.get_nodes_values()
        )
        self.assertEqual(16, self.ol.len())

    def test_add_in_head(self) -> None:

        self.assertIsNone(self.ol.find(-100))
        self.assertIsNone(self.ol.find(-500))
        self.assertNotEqual(-100, self.ol.head.value)
        self.assertNotEqual(-500, self.ol.head.value)

        self.ol.add(-100)
        self.assertIsNotNone(self.ol.find(-100))
        self.assertEqual(-100, self.ol.head.value)
        self.assertEqual(7, self.ol.len())

        self.ol.add(-500)
        self.assertIsNotNone(self.ol.find(-500))
        self.assertEqual(-500, self.ol.head.value)
        self.assertEqual(8, self.ol.len())

    def test_add_in_tail(self) -> None:

        self.assertIsNone(self.ol.find(100500))
        self.assertIsNone(self.ol.find(999999))
        self.assertNotEqual(100500, self.ol.tail.value)
        self.assertNotEqual(999999, self.ol.tail.value)

        self.ol.add(100500)
        self.assertIsNotNone(self.ol.find(100500))
        self.assertEqual(100500, self.ol.tail.value)
        self.assertEqual(7, self.ol.len())

        self.ol.add(999999)
        self.assertIsNotNone(self.ol.find(999999))
        self.assertEqual(999999, self.ol.tail.value)
        self.assertEqual(8, self.ol.len())

    def test_stress(self):

        for i in range(10000):
            self.ol.add(i)
