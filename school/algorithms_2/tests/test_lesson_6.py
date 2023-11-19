from unittest import TestCase

from algorithms_2.lesson_6 import BalancedBST


class TestLesson6(TestCase):

    def test_generate_tree(self):

        tree = BalancedBST()
        tree.GenerateTree([1, 2, 3, 4, 5, 6, 7])

        self.assertEqual(4, tree.Root.NodeKey)
        self.assertEqual(0, tree.Root.Level)
        self.assertEqual(2, tree.Root.LeftChild.NodeKey)
        self.assertEqual(1, tree.Root.LeftChild.Level)
        self.assertEqual(1, tree.Root.LeftChild.LeftChild.NodeKey)
        self.assertEqual(2, tree.Root.LeftChild.LeftChild.Level)
        self.assertEqual(3, tree.Root.LeftChild.RightChild.NodeKey)
        self.assertEqual(2, tree.Root.LeftChild.RightChild.Level)
        self.assertEqual(6, tree.Root.RightChild.NodeKey)
        self.assertEqual(1, tree.Root.RightChild.Level)
        self.assertEqual(5, tree.Root.RightChild.LeftChild.NodeKey)
        self.assertEqual(2, tree.Root.RightChild.LeftChild.Level)
        self.assertEqual(7, tree.Root.RightChild.RightChild.NodeKey)
        self.assertEqual(2, tree.Root.RightChild.RightChild.Level)

        tree_2 = BalancedBST()
        tree_2.GenerateTree([1, 4, 4, 4, 5, 4, 4, 8, -10, 2, 2, 2])

        self.assertEqual(4, tree_2.Root.NodeKey)
        self.assertEqual(0, tree_2.Root.Level)
        self.assertEqual(2, tree_2.Root.LeftChild.NodeKey)
        self.assertEqual(1, tree_2.Root.LeftChild.Level)
        self.assertEqual(1, tree_2.Root.LeftChild.LeftChild.NodeKey)
        self.assertEqual(2, tree_2.Root.LeftChild.LeftChild.Level)
        self.assertEqual(-10, tree_2.Root.LeftChild.LeftChild.LeftChild.NodeKey)
        self.assertEqual(3, tree_2.Root.LeftChild.LeftChild.LeftChild.Level)
        self.assertEqual(2, tree_2.Root.LeftChild.RightChild.NodeKey)
        self.assertEqual(2, tree_2.Root.LeftChild.RightChild.Level)
        self.assertEqual(2, tree_2.Root.LeftChild.RightChild.RightChild.NodeKey)
        self.assertEqual(3, tree_2.Root.LeftChild.RightChild.RightChild.Level)

        self.assertEqual(4, tree_2.Root.RightChild.NodeKey)
        self.assertEqual(1, tree_2.Root.RightChild.Level)
        self.assertEqual(4, tree_2.Root.RightChild.RightChild.NodeKey)
        self.assertEqual(2, tree_2.Root.RightChild.RightChild.Level)
        self.assertEqual(5, tree_2.Root.RightChild.RightChild.RightChild.NodeKey)
        self.assertEqual(3, tree_2.Root.RightChild.RightChild.RightChild.Level)
        self.assertEqual(4, tree_2.Root.RightChild.RightChild.RightChild.LeftChild.NodeKey)
        self.assertEqual(4, tree_2.Root.RightChild.RightChild.RightChild.LeftChild.Level)
        self.assertEqual(4, tree_2.Root.RightChild.RightChild.RightChild.LeftChild.RightChild.NodeKey)
        self.assertEqual(5, tree_2.Root.RightChild.RightChild.RightChild.LeftChild.RightChild.Level)
        self.assertEqual(8, tree_2.Root.RightChild.RightChild.RightChild.RightChild.NodeKey)
        self.assertEqual(4, tree_2.Root.RightChild.RightChild.RightChild.RightChild.Level)

    def test_is_balanced(self):

        tree = BalancedBST()
        tree.GenerateTree([1, 2, 3, 4, 5, 6, 7])

        self.assertTrue(tree.IsBalanced(tree.Root))

        tree_2 = BalancedBST()
        tree_2.GenerateTree([1, 4, 4, 4, 5, 4, 4, 8, -10, 2, 2, 2])

        self.assertFalse(tree_2.IsBalanced(tree_2.Root))


