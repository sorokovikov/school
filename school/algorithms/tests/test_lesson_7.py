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

        self.one_element_ol = OrderedList(True)
        self.one_element_ol.add(100)

    def test_len(self) -> None:

        self.assertEqual(6, self.ol.len())
        self.ol.add(10)
        self.ol.add(10)
        self.ol.add(10)
        self.assertEqual(9, self.ol.len())

        self.assertEqual(1, self.one_element_ol.len())

    def test_get_values(self) -> None:

        self.assertEqual([1, 100, 345, 500, 999, 100000], self.ol.get_nodes_values())
        self.assertEqual(1, self.ol.head.value)
        self.assertEqual(100000, self.ol.tail.value)

        self.ol.add(99999)
        self.assertEqual([1, 100, 345, 500, 999, 99999, 100000], self.ol.get_nodes_values())

        self.assertEqual([100], self.one_element_ol.get_nodes_values())

    def test_find(self) -> None:

        self.assertIsNone(self.ol.find(100500))
        self.assertIsNone(self.ol.find(99))
        self.assertIsNotNone(self.ol.find(999))
        self.assertIsNotNone(self.ol.find(1))

        self.ol.add(100500)
        self.assertIsNotNone(self.ol.find(100500))
        self.assertEqual([1, 100, 345, 500, 999, 100000, 100500], self.ol.get_nodes_values())

        self.assertIsNotNone(self.one_element_ol.find(100))
        self.assertIsNone(self.one_element_ol.find(2))

    def test_delete(self) -> None:

        self.ol.delete(999)
        self.assertIsNone(self.ol.find(999))
        self.assertEqual(1, self.ol.head.value)
        self.assertEqual(100000, self.ol.tail.value)
        self.assertEqual([1, 100, 345, 500, 100000], self.ol.get_nodes_values())

        self.ol.delete(1)
        self.ol.delete(100000)
        self.assertIsNone(self.ol.find(1))
        self.assertIsNone(self.ol.find(100000))
        self.assertEqual(100, self.ol.head.value)
        self.assertEqual(500, self.ol.tail.value)
        self.assertEqual([100, 345, 500], self.ol.get_nodes_values())

        self.one_element_ol.delete(100)
        self.assertIsNone(self.one_element_ol.head)
        self.assertIsNone(self.one_element_ol.tail)

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

        self.one_element_ol.add(-10)
        self.assertIsNotNone(self.one_element_ol.find(-10))
        self.assertEqual(-10, self.one_element_ol.head.value)
        self.assertEqual(100, self.one_element_ol.tail.value)
        self.assertEqual(2, self.one_element_ol.len())

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

        self.one_element_ol.add(999)
        self.assertIsNotNone(self.one_element_ol.find(999))
        self.assertEqual(100, self.one_element_ol.head.value)
        self.assertEqual(999, self.one_element_ol.tail.value)
        self.assertEqual(2, self.one_element_ol.len())

    def test_stress(self):

        for i in range(100000):
            self.ol.add(i)


class TestOrderedListDesc(TestCase):

    def setUp(self) -> None:

        self.ol = OrderedList(False)
        self.ol.add(999)
        self.ol.add(1000)
        self.ol.add(1)
        self.ol.add(-5)
        self.ol.add(300)
        self.ol.add(555)

    def test_get_values(self):

        self.assertEqual([1000, 999, 555, 300, 1, -5], self.ol.get_nodes_values())
        self.assertEqual(6, self.ol.len())
        self.assertEqual(1000, self.ol.head.value)
        self.assertEqual(-5, self.ol.tail.value)

    def test_add_in_head(self):

        self.ol.add(100500)
        self.assertEqual([100500, 1000, 999, 555, 300, 1, -5], self.ol.get_nodes_values())
        self.assertEqual(7, self.ol.len())
        self.assertEqual(100500, self.ol.head.value)
        self.assertEqual(-5, self.ol.tail.value)

    def test_add_in_tail(self):

        self.ol.add(-100)
        self.assertEqual([1000, 999, 555, 300, 1, -5, -100], self.ol.get_nodes_values())
        self.assertEqual(7, self.ol.len())
        self.assertEqual(1000, self.ol.head.value)
        self.assertEqual(-100, self.ol.tail.value)

    def test_delete_head(self):

        self.ol.delete(1000)
        self.assertEqual([999, 555, 300, 1, -5], self.ol.get_nodes_values())
        self.assertEqual(5, self.ol.len())
        self.assertEqual(999, self.ol.head.value)
        self.assertEqual(-5, self.ol.tail.value)

    def test_delete_tail(self):

        self.ol.delete(-5)
        self.assertEqual([1000, 999, 555, 300, 1], self.ol.get_nodes_values())
        self.assertEqual(5, self.ol.len())
        self.assertEqual(1000, self.ol.head.value)
        self.assertEqual(1, self.ol.tail.value)


class TestOrderedStringList(TestCase):

    def setUp(self) -> None:

        self.osl = OrderedStringList(True)
        self.osl.add("hello")
        self.osl.add("world")
        self.osl.add("foo")
        self.osl.add("bar")
        self.osl.add("baa")
        self.osl.add("   baar   ")
        self.osl.add("   ba  ar   ")

    def test_get_values(self):

        self.assertEqual(["   ba  ar   ", "baa", "   baar   ", "bar", "foo", "hello", "world"], self.osl.get_nodes_values())
        self.assertEqual(7, self.osl.len())
        self.assertEqual("   ba  ar   ", self.osl.head.value)
        self.assertEqual("world", self.osl.tail.value)

    def test_add_in_head(self):

        self.osl.add("  aaaa")
        self.assertEqual(8, self.osl.len())
        self.assertEqual(["  aaaa", "   ba  ar   ", "baa", "   baar   ", "bar", "foo", "hello", "world"], self.osl.get_nodes_values())
        self.assertEqual("  aaaa", self.osl.head.value)
        self.assertEqual("world", self.osl.tail.value)

    def test_add_in_tail(self):

        self.osl.add("yyyy  ")
        self.assertEqual(8, self.osl.len())
        self.assertEqual(["   ba  ar   ", "baa", "   baar   ", "bar", "foo", "hello", "world", "yyyy  "], self.osl.get_nodes_values())
        self.assertEqual("   ba  ar   ", self.osl.head.value)
        self.assertEqual("yyyy  ", self.osl.tail.value)

    def test_delete_head(self):

        self.osl.delete("   ba  ar   ")
        self.assertEqual(6, self.osl.len())
        self.assertEqual(["baa", "   baar   ", "bar", "foo", "hello", "world"], self.osl.get_nodes_values())
        self.assertIsNone(self.osl.find("   ba  ar   "))
        self.assertEqual("baa", self.osl.head.value)
        self.assertEqual("world", self.osl.tail.value)

    def test_delete_tail(self):

        self.osl.delete("world")
        self.assertEqual(6, self.osl.len())
        self.assertEqual(["   ba  ar   ", "baa", "   baar   ", "bar", "foo", "hello"], self.osl.get_nodes_values())
        self.assertIsNone(self.osl.find("world"))
        self.assertEqual("   ba  ar   ", self.osl.head.value)
        self.assertEqual("hello", self.osl.tail.value)


class TestOrderedStringListDesc(TestCase):

    def setUp(self) -> None:

        self.osl = OrderedStringList(False)
        self.osl.add("  yyellow")
        self.osl.add("yellow")
        self.osl.add("hello")
        self.osl.add("world")
        self.osl.add("foo")
        self.osl.add("bar")
        self.osl.add("baa")

    def test_get_values(self):

        self.assertEqual(["  yyellow", "yellow", "world", "hello", "foo", "bar", "baa"], self.osl.get_nodes_values())
        self.assertEqual(7, self.osl.len())
        self.assertEqual("  yyellow", self.osl.head.value)
        self.assertEqual("baa", self.osl.tail.value)

    def test_add_in_head(self):

        self.osl.add("zero")
        self.assertEqual(8, self.osl.len())
        self.assertEqual(["zero", "  yyellow", "yellow", "world", "hello", "foo", "bar", "baa"], self.osl.get_nodes_values())
        self.assertEqual("zero", self.osl.head.value)
        self.assertEqual("baa", self.osl.tail.value)

    def test_add_in_tail(self):

        self.osl.add("assert")
        self.assertEqual(8, self.osl.len())
        self.assertEqual(["  yyellow", "yellow", "world", "hello", "foo", "bar", "baa", "assert"], self.osl.get_nodes_values())
        self.assertEqual("  yyellow", self.osl.head.value)
        self.assertEqual("assert", self.osl.tail.value)

    def test_delete_head(self):

        self.osl.delete("  yyellow")
        self.assertEqual(6, self.osl.len())
        self.assertEqual(["yellow", "world", "hello", "foo", "bar", "baa"], self.osl.get_nodes_values())
        self.assertIsNone(self.osl.find("  yyellow"))
        self.assertEqual("yellow", self.osl.head.value)
        self.assertEqual("baa", self.osl.tail.value)

    def test_delete_tail(self):

        self.osl.delete("baa")
        self.assertEqual(6, self.osl.len())
        self.assertEqual(["  yyellow", "yellow", "world", "hello", "foo", "bar"], self.osl.get_nodes_values())
        self.assertIsNone(self.osl.find("baa"))
        self.assertEqual("  yyellow", self.osl.head.value)
        self.assertEqual("bar", self.osl.tail.value)

