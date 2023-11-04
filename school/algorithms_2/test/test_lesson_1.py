from random import randint
from unittest import TestCase

from algorithms_2.lesson_1 import SimpleTree, SimpleTreeNode


class TestLesson1(TestCase):

    def setUp(self):

        self.t = SimpleTree(SimpleTreeNode(10, None))

    def test_count(self):

        self.assertEqual(1, self.t.Count())

        parent = self.t.Root

        for i in range(29):
            child = SimpleTreeNode(i, None)
            self.t.AddChild(parent, child)
            parent = child

        self.assertEqual(30, self.t.Count())

    def test_leaf_nodes(self):

        self.assertEqual(1, self.t.LeafCount())
        parent = self.t.Root

        for i in range(29):
            child = SimpleTreeNode(i, None)
            self.t.AddChild(parent, child)
            parent = child

        self.assertEqual(1, self.t.LeafCount())

        child_1 = SimpleTreeNode(100, None)
        child_1.add_child(SimpleTreeNode(100, child_1))
        child_1.add_child(SimpleTreeNode(100, child_1))
        child_1.add_child(SimpleTreeNode(100, child_1))
        child_1.add_child(SimpleTreeNode(100, child_1))

        self.t.AddChild(self.t.Root, child_1)
        self.assertEqual(5, self.t.LeafCount())

    def test_add_child(self):

        child = SimpleTreeNode(100, None)
        self.t.AddChild(self.t.Root, child)
        self.assertEqual(2, self.t.Count())
        self.assertIn(child, self.t.Root.Children)

    def test_delete_node(self):

        tail = None
        parent = self.t.Root
        for i in range(100):
            tail = SimpleTreeNode(100, None)
            self.t.AddChild(parent, tail)
            parent = tail

        self.assertEqual(101, self.t.Count())

        tail_2 = None
        for i in range(100):
            tail_2 = SimpleTreeNode(100, None)
            self.t.AddChild(parent, tail_2)
            parent = tail_2

        self.assertEqual(201, self.t.Count())

        self.t.DeleteNode(tail)
        self.assertEqual(100, self.t.Count())

    def test_find_nodes_by_value(self):

        tail = None
        parent = self.t.Root
        for i in range(100):
            tail = SimpleTreeNode(100, None)
            self.t.AddChild(parent, tail)
            parent = tail

        self.assertEqual(101, self.t.Count())
        self.assertEqual(100, len(self.t.FindNodesByValue(100)))

        for i in range(200):
            tail = SimpleTreeNode(200, None)
            self.t.AddChild(parent, tail)
            parent = tail

        self.assertEqual(301, self.t.Count())
        self.assertEqual(100, len(self.t.FindNodesByValue(100)))
        self.assertEqual(200, len(self.t.FindNodesByValue(200)))
        self.assertEqual(1, len(self.t.FindNodesByValue(10)))

    def test_move_node(self):

        tail = None
        parent = self.t.Root
        for i in range(100):
            tail = SimpleTreeNode(100, None)
            self.t.AddChild(parent, tail)
            parent = tail

        parent_2 = parent

        for i in range(200):
            tail = SimpleTreeNode(200, None)
            self.t.AddChild(parent_2, tail)
            parent_2 = tail

        self.assertEqual(301, self.t.Count())
        parent_3 = parent.Parent
        self.assertIn(parent, parent_3.Children)
        self.t.MoveNode(parent, self.t.Root)
        self.assertEqual(301, self.t.Count())
        self.assertNotIn(parent, parent_3.Children)
        self.assertIn(parent, self.t.Root.Children)

    def test_stress(self):

        parent = self.t.Root

        for i in range(1000):
            child = SimpleTreeNode(i, None)
            self.t.AddChild(parent, child)
            r = randint(0, 10)
            if r < 7:
                parent = child

        self.assertEqual(1001, self.t.Count())
