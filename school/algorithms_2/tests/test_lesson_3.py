from unittest import TestCase

from algorithms_2.lesson_3 import BSTNode, BST


class TestLesson2(TestCase):

    def setUp(self):

        self.t = BST(BSTNode(10, 10, None))
        self.t.AddKeyValue(20, 20)
        self.t.AddKeyValue(30, 30)
        self.t.AddKeyValue(5, 5)
        self.t.AddKeyValue(15, 15)
        self.t.AddKeyValue(2, 2)
        self.t.AddKeyValue(7, 7)

    def test_wide_nodes(self) -> None:

        all_nodes = self.t.WideAllNodes()
        expected_keys = [10, 5, 20, 2, 7, 15, 30]

        self.assertEqual(len(expected_keys), len(all_nodes))
        self.assertListEqual(expected_keys, [node.NodeKey for node in all_nodes])

    def test_in_order(self):

        all_nodes = self.t.DeepAllNodes(0)
        expected_keys = [2, 5, 7, 10, 15, 20, 30]

        self.assertEqual(len(expected_keys), len(all_nodes))
        self.assertListEqual(expected_keys, [node.NodeKey for node in all_nodes])

    def test_post_order(self):

        all_nodes = self.t.DeepAllNodes(1)
        expected_keys = [2, 7, 5, 15, 30, 20, 10]

        self.assertEqual(len(expected_keys), len(all_nodes))
        self.assertListEqual(expected_keys, [node.NodeKey for node in all_nodes])

    def test_pre_order(self):

        all_nodes = self.t.DeepAllNodes(2)
        expected_keys = [10, 5, 2, 7, 20, 15, 30]

        self.assertEqual(len(expected_keys), len(all_nodes))
        self.assertListEqual(expected_keys, [node.NodeKey for node in all_nodes])
