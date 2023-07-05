from unittest import TestCase

from algorithms.lesson_2_additional import LinkedListDummyNode, LinkedListDummyNodes, Node


class TestLinkedListDummyNodes(TestCase):

    def setUp(self) -> None:

        self.ll = LinkedListDummyNodes()
        self.ll.add_in_tail(Node(1))
        self.ll.add_in_tail(Node(1))
        self.ll.add_in_tail(Node(2))
        self.ll.add_in_tail(Node(2))
        self.ll.add_in_tail(Node(3))
        self.ll.add_in_tail(Node(3))

        self.one_element_ll = LinkedListDummyNodes()
        self.one_element_ll.add_in_tail(Node(1))

        self.empty_ll = LinkedListDummyNodes()

    def get_ll_values(self) -> list:

        return [node.value for node in self.ll]

    def test_add_in_head(self):

        expected_values = [-100, 999, 1, 1, 2, 2, 3, 3]
        self.ll.add_in_head(Node(999))
        self.ll.add_in_head(Node(-100))
        self.assertEqual(expected_values, self.get_ll_values())

    def test_add_in_tail(self):

        expected_values = [1, 1, 2, 2, 3, 3, 999, -100]
        self.ll.add_in_tail(Node(999))
        self.ll.add_in_tail(Node(-100))
        self.assertEqual(expected_values, self.get_ll_values())

    def test_find_all(self):

        found_nodes = self.ll.find_all(1)
        self.assertEqual(2, len(found_nodes))

        self.ll.add_in_tail(Node(2))
        found_nodes = self.ll.find_all(2)
        self.assertEqual(3, len(found_nodes))

        self.ll.delete(3)
        found_nodes = self.ll.find_all(3)
        self.assertEqual(1, len(found_nodes))

        found_nodes = self.ll.find_all(999)
        self.assertEqual(0, len(found_nodes))

        found_nodes = self.one_element_ll.find_all(0)
        self.assertEqual(0, len(found_nodes))

        found_nodes = self.one_element_ll.find_all(1)
        self.assertEqual(1, len(found_nodes))

        found_nodes = self.empty_ll.find_all(0)
        self.assertEqual(0, len(found_nodes))

    def test_len(self):

        self.assertEqual(6, self.ll.len())
        self.assertEqual(1, self.one_element_ll.len())
        self.assertEqual(0, self.empty_ll.len())

        self.ll.add_in_tail(Node(999))
        self.ll.add_in_tail(Node(100))
        self.assertEqual(8, self.ll.len())

    def test_delete_in_start(self):

        expected_values = [1, 2, 2, 3, 3]
        self.ll.delete(1)
        self.assertEqual(expected_values, self.get_ll_values())

    def test_delete_all_in_start(self):

        expected_values = [2, 2, 3, 3]
        self.ll.delete(1, True)
        self.assertEqual(expected_values, self.get_ll_values())

    def test_delete_in_middle(self):

        expected_values = [1, 1, 2, 3, 3]
        self.ll.delete(2)
        self.assertEqual(expected_values, self.get_ll_values())

    def test_delete_all_in_middle(self):

        expected_values = [1, 1, 3, 3]
        self.ll.delete(2, True)
        self.assertEqual(expected_values, self.get_ll_values())

    def test_delete_in_tail(self):

        expected_values = [1, 1, 2, 2, 3]
        self.ll.delete(3)
        self.assertEqual(expected_values, self.get_ll_values())

    def test_delete_all_in_tail(self):

        expected_values = [1, 1, 2, 2]
        self.ll.delete(3, True)
        self.assertEqual(expected_values, self.get_ll_values())


class TestLinkedListDummyNode(TestCase):

    def setUp(self) -> None:

        self.ll = LinkedListDummyNode()
        self.ll.add_in_tail(Node(1))
        self.ll.add_in_tail(Node(1))
        self.ll.add_in_tail(Node(2))
        self.ll.add_in_tail(Node(2))
        self.ll.add_in_tail(Node(3))
        self.ll.add_in_tail(Node(3))

        self.one_element_ll = LinkedListDummyNode()
        self.one_element_ll.add_in_tail(Node(1))

        self.empty_ll = LinkedListDummyNode()

    def test_setup(self):

        expected_values = [1, 1, 2, 2, 3, 3]
        self.assertEqual(expected_values, self.ll.get_nodes_values())

    def test_add_in_head(self):

        expected_values = [-100, 999, 1, 1, 2, 2, 3, 3]
        self.ll.add_in_head(Node(999))
        self.ll.add_in_head(Node(-100))
        self.assertEqual(expected_values, self.ll.get_nodes_values())

    def test_add_in_tail(self):

        expected_values = [1, 1, 2, 2, 3, 3, 999, -100]
        self.ll.add_in_tail(Node(999))
        self.ll.add_in_tail(Node(-100))
        self.assertEqual(expected_values, self.ll.get_nodes_values())

    def test_len(self):

        self.assertEqual(6, self.ll.len())
        self.assertEqual(1, self.one_element_ll.len())
        self.assertEqual(0, self.empty_ll.len())

        self.ll.add_in_tail(Node(999))
        self.ll.add_in_tail(Node(100))
        self.assertEqual(8, self.ll.len())

    def test_delete_in_start(self):

        expected_values = [1, 2, 2, 3, 3]
        self.ll.delete(1)
        self.assertEqual(expected_values, self.ll.get_nodes_values())

    def test_delete_all_in_start(self):

        expected_values = [2, 2, 3, 3]
        self.ll.delete(1, True)
        self.assertEqual(expected_values, self.ll.get_nodes_values())

    def test_delete_in_middle(self):

        expected_values = [1, 1, 2, 3, 3]
        self.ll.delete(2)
        self.assertEqual(expected_values, self.ll.get_nodes_values())

    def test_delete_all_in_middle(self):

        expected_values = [1, 1, 3, 3]
        self.ll.delete(2, True)
        self.assertEqual(expected_values, self.ll.get_nodes_values())

    def test_delete_in_tail(self):

        expected_values = [1, 1, 2, 2, 3]
        self.ll.delete(3)
        self.assertEqual(expected_values, self.ll.get_nodes_values())

    def test_delete_all_in_tail(self):

        expected_values = [1, 1, 2, 2]
        self.ll.delete(3, True)
        self.assertEqual(expected_values, self.ll.get_nodes_values())

    def test_insert_in_start(self):

        expected_values = [999, -100]
        node = Node(999)
        self.empty_ll.insert(None, node)
        self.empty_ll.insert(node, Node(-100))
        self.assertEqual(expected_values, self.empty_ll.get_nodes_values())

    def test_insert_in_middle(self):

        expected_values = [999, -100, 555, 1, 1, 2, 2, 3, 3]

        node = Node(999)
        node_2 = Node(-100)
        self.ll.add_in_head(node)
        self.ll.insert(node, node_2)
        self.ll.insert(node_2, Node(555))

        self.assertEqual(expected_values, self.ll.get_nodes_values())

    def test_insert_in_tail(self):

        expected_values = [1, 1, 2, 2, 3, 3, 999, -100, 555]

        node = Node(999)
        node_2 = Node(-100)
        self.ll.add_in_tail(node)
        self.ll.insert(node, node_2)
        self.ll.insert(node_2, Node(555))

        self.assertEqual(expected_values, self.ll.get_nodes_values())

    def test_clean(self):

        self.ll.clean()

        self.assertEqual(0, self.ll.len())
        self.assertEqual(self.ll.dummy_node, self.ll.dummy_node.next)
        self.assertEqual(self.ll.dummy_node, self.ll.dummy_node.prev)
