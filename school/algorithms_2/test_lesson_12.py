from unittest import TestCase

from algorithms_2.lesson_12 import SimpleGraph


class TestLesson8(TestCase):

    def setUp(self):

        self.sg = SimpleGraph(9)

        # Vertices
        self.sg.AddVertex(1)
        self.sg.AddVertex(2)
        self.sg.AddVertex(3)
        self.sg.AddVertex(4)
        self.sg.AddVertex(5)
        self.sg.AddVertex(6)
        self.sg.AddVertex(7)
        self.sg.AddVertex(8)
        self.sg.AddVertex(9)

        # Edges
        self.sg.AddEdge(0, 1)
        self.sg.AddEdge(0, 3)
        self.sg.AddEdge(0, 4)
        self.sg.AddEdge(1, 5)
        self.sg.AddEdge(2, 5)
        self.sg.AddEdge(2, 7)
        self.sg.AddEdge(3, 4)
        self.sg.AddEdge(3, 6)
        self.sg.AddEdge(4, 5)
        self.sg.AddEdge(4, 6)
        self.sg.AddEdge(5, 7)
        self.sg.AddEdge(7, 8)

    def test_weak_vertices(self):

        result = self.sg.WeakVertices()
        self.assertNotEquals([], result)
        expected_vertices = [2, 9]
        for i in result:
            with self.subTest():
                self.assertIn(i.Value, expected_vertices)

        self.sg.RemoveEdge(2, 7)

        result = self.sg.WeakVertices()
        self.assertNotEquals([], result)
        expected_vertices = [2, 3, 6, 8, 9]
        for i in result:
            with self.subTest():
                self.assertIn(i.Value, expected_vertices)

        self.sg.AddEdge(5, 8)

        result = self.sg.WeakVertices()
        self.assertNotEquals([], result)
        expected_vertices = [2, 3]
        for i in result:
            with self.subTest():
                self.assertIn(i.Value, expected_vertices)

        self.sg.RemoveEdge(3, 4)

        result = self.sg.WeakVertices()
        self.assertNotEquals([], result)
        expected_vertices = [1, 2, 3, 4, 5, 7]
        for i in result:
            with self.subTest():
                self.assertIn(i.Value, expected_vertices)
