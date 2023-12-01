from unittest import TestCase

from algorithms_2.lesson_9 import SimpleTree, SimpleTreeNode


class TestLesson9(TestCase):

    def test_even_trees(self):

        st = SimpleTree(SimpleTreeNode(1, None))

        st.AddChild(st.Root, SimpleTreeNode(2, None))
        st.AddChild(st.Root, SimpleTreeNode(3, None))
        st.AddChild(st.Root, SimpleTreeNode(6, None))

        st.AddChild(st.Root.Children[0], SimpleTreeNode(5, None))
        st.AddChild(st.Root.Children[0], SimpleTreeNode(7, None))
        st.AddChild(st.Root.Children[0], SimpleTreeNode(11, None))

        st.AddChild(st.Root.Children[1], SimpleTreeNode(4, None))

        st.AddChild(st.Root.Children[2], SimpleTreeNode(8, None))
        st.AddChild(st.Root.Children[2].Children[0], SimpleTreeNode(9, None))
        st.AddChild(st.Root.Children[2].Children[0], SimpleTreeNode(10, None))

        node_pairs = st.EvenTrees()
        self.assertListEqual([1, 3, 1, 6], [node.NodeValue for node in node_pairs])




