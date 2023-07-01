from unittest import TestCase

from algorithms.lesson_1 import LinkedList, Node


class TestLessonOne(TestCase):

    def setUp(self) -> None:

        self.ll = LinkedList()
        self.ll.add_in_tail(Node(100))
        self.ll.add_in_tail(Node(100))
        self.ll.add_in_tail(Node(200))
        self.ll.add_in_tail(Node(300))
        self.ll.add_in_tail(Node(300))
        self.ll.add_in_tail(Node(100))

    def test_delete_200(self):

        expected_ll = LinkedList()
        expected_ll.add_in_tail(Node(100))
        expected_ll.add_in_tail(Node(100))
        expected_ll.add_in_tail(Node(300))
        expected_ll.add_in_tail(Node(300))
        expected_ll.add_in_tail(Node(100))

        self.ll.delete(200)
        self.assertEqual(self.ll, expected_ll)

    def test_delete_all_100(self):

        expected_ll = LinkedList()
        expected_ll.add_in_tail(Node(200))
        expected_ll.add_in_tail(Node(300))
        expected_ll.add_in_tail(Node(300))

        self.ll.delete(100, True)
        self.assertEqual(self.ll, expected_ll)

    def test_delete_200_and_300(self):

        expected_ll = LinkedList()
        expected_ll.add_in_tail(Node(100))
        expected_ll.add_in_tail(Node(100))
        expected_ll.add_in_tail(Node(300))
        expected_ll.add_in_tail(Node(100))

        self.ll.delete(200)
        self.ll.delete(300)

        self.assertEqual(self.ll, expected_ll)

    def test_delete_all_300(self):

        expected_ll = LinkedList()
        expected_ll.add_in_tail(Node(100))
        expected_ll.add_in_tail(Node(100))
        expected_ll.add_in_tail(Node(200))
        expected_ll.add_in_tail(Node(100))

        self.ll.delete(300, True)

        self.assertEqual(self.ll, expected_ll)

    def test_delete_9999(self):

        expected_ll = LinkedList()
        expected_ll.add_in_tail(Node(100))
        expected_ll.add_in_tail(Node(100))
        expected_ll.add_in_tail(Node(200))
        expected_ll.add_in_tail(Node(300))
        expected_ll.add_in_tail(Node(300))
        expected_ll.add_in_tail(Node(100))

        self.ll.delete(9999, True)

        self.assertEqual(self.ll, expected_ll)

    def test_clean(self):

        self.ll.clean()

        self.assertEqual(self.ll.len(), 0)

    def test_len(self):

        self.assertEqual(self.ll.len(), 6)

        self.ll.delete(200)
        self.assertEqual(self.ll.len(), 5)

        self.ll.delete(100, True)
        self.assertEqual(self.ll.len(), 2)

    def test_find_all(self):

        found_node = self.ll.find_all(200)
        self.assertEqual(len(found_node), 1)

        found_nodes = self.ll.find_all(100)
        self.assertEqual(len(found_nodes), 3)

    def test_insert_in_start(self):

        expected_ll = LinkedList()
        expected_ll.add_in_tail(Node(999))
        expected_ll.add_in_tail(Node(1))
        expected_ll.add_in_tail(Node(100))
        expected_ll.add_in_tail(Node(100))
        expected_ll.add_in_tail(Node(200))
        expected_ll.add_in_tail(Node(300))
        expected_ll.add_in_tail(Node(300))
        expected_ll.add_in_tail(Node(100))

        self.ll.insert(None, Node(1))
        self.ll.insert(None, Node(999))

        self.assertEqual(self.ll, expected_ll)

    def test_insert_in_middle(self):

        expected_ll = LinkedList()
        expected_ll.add_in_tail(Node(100))
        expected_ll.add_in_tail(Node(100))
        expected_ll.add_in_tail(Node(200))
        expected_ll.add_in_tail(Node(1))
        expected_ll.add_in_tail(Node(300))
        expected_ll.add_in_tail(Node(300))
        expected_ll.add_in_tail(Node(100))

        found_node = self.ll.find(200)
        self.ll.insert(found_node, Node(1))
        self.assertEqual(self.ll, expected_ll)

    def test_insert_in_tail(self):

        expected_ll = LinkedList()
        expected_ll.add_in_tail(Node(100))
        expected_ll.add_in_tail(Node(100))
        expected_ll.add_in_tail(Node(200))
        expected_ll.add_in_tail(Node(300))
        expected_ll.add_in_tail(Node(300))
        expected_ll.add_in_tail(Node(100))
        expected_ll.add_in_tail(Node(1))
        expected_ll.add_in_tail(Node(999))

        found_nodes = self.ll.find_all(100)
        node_1 = Node(1)
        node_2 = Node(999)

        self.ll.insert(found_nodes[2], node_1)
        self.ll.insert(node_1, node_2)

        self.assertEqual(self.ll, expected_ll)
