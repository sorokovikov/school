from unittest import TestCase

from algorithms_2.lesson_11 import SimpleGraph


class TestLesson8(TestCase):

    def setUp(self):

        self.sg = SimpleGraph(9)

        # Vertices
        self.sg.AddVertex(10)
        self.sg.AddVertex(5)
        self.sg.AddVertex(3)
        self.sg.AddVertex(23)
        self.sg.AddVertex(2)
        self.sg.AddVertex(7)
        self.sg.AddVertex(1)
        self.sg.AddVertex(8)  # 7
        self.sg.AddVertex(9)  # 8

        # Edges
        self.sg.AddEdge(0, 1)
        self.sg.AddEdge(0, 2)
        self.sg.AddEdge(0, 3)
        self.sg.AddEdge(1, 3)
        self.sg.AddEdge(2, 4)
        self.sg.AddEdge(1, 5)
        self.sg.AddEdge(4, 6)
        self.sg.AddEdge(5, 7)

    def test_depth_first_search(self):

        result = self.sg.BreadthFirstSearch(0, 4)
        self.assertListEqual([10, 3, 2], [vertex.Value for vertex in result])

        result = self.sg.BreadthFirstSearch(0, 7)
        self.assertListEqual([10, 5, 7, 8], [vertex.Value for vertex in result])

        result = self.sg.BreadthFirstSearch(-1, 4)
        self.assertListEqual([], [vertex.Value for vertex in result])
        result = self.sg.BreadthFirstSearch(0, 1000)
        self.assertListEqual([], [vertex.Value for vertex in result])
        result = self.sg.BreadthFirstSearch(6, 4)
        self.assertListEqual([1, 2], [vertex.Value for vertex in result])

        result = self.sg.BreadthFirstSearch(0, 8)
        self.assertListEqual([], [vertex.Value for vertex in result])
