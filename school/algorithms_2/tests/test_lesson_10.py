from unittest import TestCase

from algorithms_2.lesson_10 import SimpleGraph


class TestLesson8(TestCase):

    def setUp(self):

        self.sg = SimpleGraph(8)

        # Vertices
        self.sg.AddVertex(10)
        self.sg.AddVertex(5)
        self.sg.AddVertex(3)
        self.sg.AddVertex(23)
        self.sg.AddVertex(2)
        self.sg.AddVertex(7)

        # Edges
        self.sg.AddEdge(0, 1)
        self.sg.AddEdge(0, 2)
        self.sg.AddEdge(0, 3)
        self.sg.AddEdge(1, 3)
        self.sg.AddEdge(2, 4)

    def test_depth_first_search(self):

        result = self.sg.DepthFirstSearch(0, 4)
        self.assertListEqual([10, 3, 2], [vertex.Value for vertex in result])

        result = self.sg.DepthFirstSearch(-1, 4)
        self.assertListEqual([], result)
        result = self.sg.DepthFirstSearch(0, 1000)
        self.assertListEqual([], result)
        result = self.sg.DepthFirstSearch(6, 4)
        self.assertListEqual([], result)
        result = self.sg.DepthFirstSearch(0, 7)
        self.assertListEqual([], result)

        result = self.sg.DepthFirstSearch(0, 5)
        self.assertListEqual([], result)
