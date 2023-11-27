from unittest import TestCase

from algorithms_2.lesson_8 import SimpleGraph


class TestLesson8(TestCase):

    def setUp(self):

        self.sg = SimpleGraph(8)

        # Vertices
        self.sg.AddVertex(10)
        self.sg.AddVertex(2)
        self.sg.AddVertex(3)
        self.sg.AddVertex(23)

        # Edges
        self.sg.AddEdge(0, 2)
        self.sg.AddEdge(0, 3)
        self.sg.AddEdge(1, 3)

    def test_is_edge(self):

        self.assertTrue(self.sg.IsEdge(0, 2))
        self.assertTrue(self.sg.IsEdge(0, 3))
        self.assertTrue(self.sg.IsEdge(1, 3))

        self.assertFalse(self.sg.IsEdge(0, 1))
        self.assertFalse(self.sg.IsEdge(1, 2))
        self.assertFalse(self.sg.IsEdge(2, 3))

        self.sg.AddEdge(2, 3)
        self.assertTrue(self.sg.IsEdge(2, 3))

        self.sg.AddVertex(100)
        self.sg.AddEdge(3, 4)
        self.assertTrue(self.sg.IsEdge(3, 4))

        self.assertFalse(self.sg.IsEdge(0, 4))
        self.assertFalse(self.sg.IsEdge(1, 4))
        self.assertFalse(self.sg.IsEdge(2, 4))

    def test_add_vertex(self):

        self.sg.AddVertex(10)

        self.assertFalse(self.sg.IsEdge(0, 4))
        self.assertFalse(self.sg.IsEdge(1, 4))
        self.assertFalse(self.sg.IsEdge(2, 4))
        self.assertFalse(self.sg.IsEdge(3, 4))

    def test_add_edge(self):

        self.assertFalse(self.sg.IsEdge(2, 3))
        self.sg.AddEdge(2, 3)
        self.assertTrue(self.sg.IsEdge(2, 3))

    def test_remove_edge(self):

        self.assertTrue(self.sg.IsEdge(0, 3))
        self.sg.RemoveEdge(0, 3)
        self.assertFalse(self.sg.IsEdge(0, 3))

    def test_remove_vertex(self):

        self.assertTrue(self.sg.IsEdge(0, 2))
        self.assertTrue(self.sg.IsEdge(0, 3))

        self.sg.RemoveVertex(0)

        self.assertFalse(self.sg.IsEdge(0, 2))
        self.assertFalse(self.sg.IsEdge(0, 3))

    def test_max_vertex(self):

        self.sg.AddVertex(-1)
        self.sg.AddVertex(-2)
        self.sg.AddVertex(-3)
        self.sg.AddVertex(-4)

        self.assertEqual(-4, self.sg.vertex[self.sg.max_vertex - 1].Value)

        self.sg.AddVertex(-5)

        self.assertEqual(-4, self.sg.vertex[self.sg.max_vertex - 1].Value)
