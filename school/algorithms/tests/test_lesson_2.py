from unittest import TestCase

from algorithms.lesson_2 import LinkedList2, Node


class TestLessonOne(TestCase):

    def setUp(self) -> None:

        self.ll = LinkedList2()
        self.ll.add_in_tail(Node(1))
        self.ll.add_in_tail(Node(1))
        self.ll.add_in_tail(Node(2))
        self.ll.add_in_tail(Node(2))
        self.ll.add_in_tail(Node(3))
        self.ll.add_in_tail(Node(4))
        self.ll.add_in_tail(Node(4))
        self.ll.add_in_tail(Node(4))

        self.one_element_ll = LinkedList2()
        self.one_element_ll.add_in_tail(Node(-1))

        self.empty_ll = LinkedList2()

    def test_delete_in_start(self):

        expected_ll = LinkedList2()
        expected_ll.add_in_tail(Node(1))
        expected_ll.add_in_tail(Node(2))
        expected_ll.add_in_tail(Node(2))
        expected_ll.add_in_tail(Node(3))
        expected_ll.add_in_tail(Node(4))
        expected_ll.add_in_tail(Node(4))
        expected_ll.add_in_tail(Node(4))

        self.ll.delete(1)
        self.assertEqual(expected_ll, self.ll)

    def test_delete_all_in_start(self):

        expected_ll = LinkedList2()
        expected_ll.add_in_tail(Node(2))
        expected_ll.add_in_tail(Node(2))
        expected_ll.add_in_tail(Node(3))
        expected_ll.add_in_tail(Node(4))
        expected_ll.add_in_tail(Node(4))
        expected_ll.add_in_tail(Node(4))

        self.ll.delete(1, True)
        self.assertEqual(expected_ll, self.ll)

    def test_delete_in_middle(self):

        expected_ll = LinkedList2()
        expected_ll.add_in_tail(Node(1))
        expected_ll.add_in_tail(Node(1))
        expected_ll.add_in_tail(Node(2))
        expected_ll.add_in_tail(Node(3))
        expected_ll.add_in_tail(Node(4))
        expected_ll.add_in_tail(Node(4))
        expected_ll.add_in_tail(Node(4))

        self.ll.delete(2)
        self.assertEqual(expected_ll, self.ll)

    def test_delete_all_in_middle(self):

        expected_ll = LinkedList2()
        expected_ll.add_in_tail(Node(1))
        expected_ll.add_in_tail(Node(1))
        expected_ll.add_in_tail(Node(3))
        expected_ll.add_in_tail(Node(4))
        expected_ll.add_in_tail(Node(4))
        expected_ll.add_in_tail(Node(4))

        self.ll.delete(2, True)
        self.assertEqual(expected_ll, self.ll)

    def test_delete_in_tail(self):

        expected_ll = LinkedList2()
        expected_ll.add_in_tail(Node(1))
        expected_ll.add_in_tail(Node(1))
        expected_ll.add_in_tail(Node(2))
        expected_ll.add_in_tail(Node(2))
        expected_ll.add_in_tail(Node(3))
        expected_ll.add_in_tail(Node(4))
        expected_ll.add_in_tail(Node(4))

        self.ll.delete(4)
        self.assertEqual(expected_ll, self.ll)

    def test_delete_all_in_tail(self):

        expected_ll = LinkedList2()
        expected_ll.add_in_tail(Node(1))
        expected_ll.add_in_tail(Node(1))
        expected_ll.add_in_tail(Node(2))
        expected_ll.add_in_tail(Node(2))
        expected_ll.add_in_tail(Node(3))

        self.ll.delete(4, True)
        self.assertEqual(expected_ll, self.ll)

    def test_delete_multiple(self):

        expected_ll = LinkedList2()
        expected_ll.add_in_tail(Node(1))
        expected_ll.add_in_tail(Node(3))
        expected_ll.add_in_tail(Node(4))
        expected_ll.add_in_tail(Node(4))

        self.ll.delete(1)
        self.ll.delete(2, True)
        self.ll.delete(4)
        self.assertEqual(expected_ll, self.ll)

    def test_delete_nonexistent(self):

        expected_ll = LinkedList2()
        expected_ll.add_in_tail(Node(1))
        expected_ll.add_in_tail(Node(1))
        expected_ll.add_in_tail(Node(2))
        expected_ll.add_in_tail(Node(2))
        expected_ll.add_in_tail(Node(3))
        expected_ll.add_in_tail(Node(4))
        expected_ll.add_in_tail(Node(4))
        expected_ll.add_in_tail(Node(4))

        self.ll.delete(999, True)
        self.assertEqual(expected_ll, self.ll)

    def test_delete_everything(self):

        expected_ll = LinkedList2()

        self.ll.delete(1, True)
        self.ll.delete(2, True)
        self.ll.delete(3, True)
        self.ll.delete(4, True)
        self.assertEqual(expected_ll, self.ll)

        self.one_element_ll.delete(-1)
        self.assertEqual(expected_ll, self.one_element_ll)

    def test_clean(self):

        expected_ll = LinkedList2()

        self.ll.clean()
        self.assertEqual(expected_ll, self.ll)

        self.one_element_ll.clean()
        self.assertEqual(expected_ll, self.one_element_ll)

        self.empty_ll.clean()
        self.assertEqual(expected_ll, self.empty_ll)

    def test_len(self):

        self.assertEqual(8, self.ll.len())

        self.ll.delete(1)
        self.assertEqual(7, self.ll.len())

        self.ll.delete(3, True)
        self.assertEqual(6, self.ll.len())

        self.ll.delete(4, True)
        self.assertEqual(3, self.ll.len())

        self.assertEqual(1, self.one_element_ll.len())
        self.assertEqual(0, self.empty_ll.len())

    def test_find_all(self):

        found_nodes = self.ll.find_all(1)
        self.assertEqual(2, len(found_nodes))

        found_nodes = self.ll.find_all(3)
        self.assertEqual(1, len(found_nodes))

        found_nodes = self.ll.find_all(4)
        self.assertEqual(3, len(found_nodes))

        found_nodes = self.ll.find_all(999)
        self.assertEqual(0, len(found_nodes))

        found_nodes = self.one_element_ll.find_all(0)
        self.assertEqual(0, len(found_nodes))

        found_nodes = self.one_element_ll.find_all(-1)
        self.assertEqual(1, len(found_nodes))

        found_nodes = self.empty_ll.find_all(0)
        self.assertEqual(0, len(found_nodes))

    def test_insert_in_start(self):

        expected_ll = LinkedList2()
        expected_ll.add_in_tail(Node(999))
        expected_ll.add_in_tail(Node(-100))
        expected_ll.add_in_tail(Node(1))
        expected_ll.add_in_tail(Node(1))
        expected_ll.add_in_tail(Node(2))
        expected_ll.add_in_tail(Node(2))
        expected_ll.add_in_tail(Node(3))
        expected_ll.add_in_tail(Node(4))
        expected_ll.add_in_tail(Node(4))
        expected_ll.add_in_tail(Node(4))

        self.ll.insert(None, Node(-100))
        self.ll.insert(None, Node(999))
        self.assertEqual(expected_ll, self.ll)

    def test_insert_in_middle(self):

        expected_ll = LinkedList2()
        expected_ll.add_in_tail(Node(1))
        expected_ll.add_in_tail(Node(1))
        expected_ll.add_in_tail(Node(2))
        expected_ll.add_in_tail(Node(2))
        expected_ll.add_in_tail(Node(3))
        expected_ll.add_in_tail(Node(999))
        expected_ll.add_in_tail(Node(4))
        expected_ll.add_in_tail(Node(4))
        expected_ll.add_in_tail(Node(4))

        found_node = self.ll.find(3)
        self.ll.insert(found_node, Node(999))
        self.assertEqual(expected_ll, self.ll)

    def test_insert_in_tail(self):

        expected_ll = LinkedList2()
        expected_ll.add_in_tail(Node(1))
        expected_ll.add_in_tail(Node(1))
        expected_ll.add_in_tail(Node(2))
        expected_ll.add_in_tail(Node(2))
        expected_ll.add_in_tail(Node(3))
        expected_ll.add_in_tail(Node(4))
        expected_ll.add_in_tail(Node(4))
        expected_ll.add_in_tail(Node(4))
        expected_ll.add_in_tail(Node(999))
        expected_ll.add_in_tail(Node(-100))

        found_nodes = self.ll.find_all(4)
        node_1 = Node(999)
        node_2 = Node(-100)

        self.ll.insert(found_nodes[2], node_1)
        self.ll.insert(node_1, node_2)

        self.assertEqual(expected_ll, self.ll)

    def test_insert_into_empty(self):

        expected_ll = LinkedList2()
        expected_ll.add_in_tail(Node(999))

        self.empty_ll.insert(None, Node(999))
        self.assertEqual(expected_ll, self.empty_ll)
