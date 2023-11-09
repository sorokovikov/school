from unittest import TestCase

from algorithms_2.lesson_2 import BSTNode, BST


class TestLesson2(TestCase):

    def setUp(self):

        self.t = BST(BSTNode(10, 10, None))
        self.t.AddKeyValue(20, 20)
        self.t.AddKeyValue(30, 30)
        self.t.AddKeyValue(5, 5)

    def test_count(self):

        self.assertEqual(4, self.t.Count())

        self.t.AddKeyValue(100, 500)
        self.t.AddKeyValue(1, 500)
        self.t.AddKeyValue(2, 500)

        self.assertEqual(7, self.t.Count())

    def test_find(self):

        find = self.t.FindNodeByKey(10)
        self.assertIs(self.t.Root, find.Node)
        self.assertTrue(find.NodeHasKey)
        self.assertEqual(10, find.Node.NodeKey)
        self.assertEqual(10, find.Node.NodeValue)
        self.assertIs(self.t.Root.LeftChild, find.Node.LeftChild)
        self.assertIs(self.t.Root.RightChild, find.Node.RightChild)

        find = self.t.FindNodeByKey(20)
        self.assertTrue(find.NodeHasKey)
        self.assertEqual(20, find.Node.NodeKey)
        self.assertEqual(20, find.Node.NodeValue)

        find = self.t.FindNodeByKey(4)
        self.assertFalse(find.NodeHasKey)
        self.assertTrue(find.ToLeft)

        find = self.t.FindNodeByKey(6)
        self.assertFalse(find.NodeHasKey)
        self.assertFalse(find.ToLeft)

    def test_add(self):

        is_added = self.t.AddKeyValue(4, 4)
        self.assertTrue(is_added)
        find = self.t.FindNodeByKey(4)
        self.assertTrue(find.NodeHasKey)
        self.assertEqual(4, find.Node.NodeKey)
        self.assertEqual(4, find.Node.NodeValue)
        self.assertIs(find.Node, find.Node.Parent.LeftChild)

        is_added = self.t.AddKeyValue(6, 6)
        self.assertTrue(is_added)
        find = self.t.FindNodeByKey(6)
        self.assertTrue(find.NodeHasKey)
        self.assertEqual(6, find.Node.NodeKey)
        self.assertEqual(6, find.Node.NodeValue)
        self.assertIs(find.Node, find.Node.Parent.RightChild)

    def test_find_min_max(self):

        self.assertEqual(5, self.t.FinMinMax(self.t.Root, False).NodeKey)
        self.assertEqual(30, self.t.FinMinMax(self.t.Root, True).NodeKey)

        self.t.AddKeyValue(6, 6)
        self.t.AddKeyValue(7, 7)
        self.t.AddKeyValue(3, 3)
        self.t.AddKeyValue(1, 1)

        self.assertEqual(1, self.t.FinMinMax(self.t.Root.LeftChild, False).NodeKey)
        self.assertEqual(7, self.t.FinMinMax(self.t.Root.LeftChild, True).NodeKey)

    def test_delete(self):

        self.t.AddKeyValue(6, 6)
        self.t.AddKeyValue(7, 7)
        self.t.AddKeyValue(1, 1)

        self.assertEqual(7, self.t.Count())

        self.t.DeleteNodeByKey(6)

        self.assertEqual(6, self.t.Count())

        find = self.t.FindNodeByKey(6)
        self.assertFalse(find.NodeHasKey)

        self.t.DeleteNodeByKey(10)

        self.assertEqual(5, self.t.Count())









