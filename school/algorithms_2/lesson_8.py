from functools import reduce
from typing import Optional


class Vertex:

    def __init__(self, val: int):
        self.Value = val


class SimpleGraph:

    def __init__(self, size: int):
        self.max_vertex: int = size
        self.m_adjacency: list[list[int]] = [[0] * size for _ in range(size)]
        self.vertex: list[Optional[Vertex]] = [None] * size

    def AddVertex(self, v: int) -> None:

        empty_index = self.__find_first_empty_vertex_slot()

        if empty_index == -1:
            return

        self.vertex[empty_index] = Vertex(v)

    def __find_first_empty_vertex_slot(self) -> int:

        free_slot_candidate = reduce(lambda x, y: x if x[1] is None else y, enumerate(self.vertex))
        if free_slot_candidate[1] is None:
            return free_slot_candidate[0]
        return -1

    # v - is index
    def RemoveVertex(self, v: int) -> None:

        if v >= self.max_vertex:
            return

        self.vertex[v] = None

        def remove_existing_edge(v2) -> None:
            if self.IsEdge(v, v2):
                self.RemoveEdge(v, v2)

        list(map(lambda v2: remove_existing_edge(v2), range(self.max_vertex)))

    def IsEdge(self, v1: int, v2: int) -> bool:

        if v1 >= self.max_vertex or v2 >= self.max_vertex:
            return False

        return self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1: int, v2: int) -> None:

        if v1 >= self.max_vertex or v2 >= self.max_vertex or self.vertex[v1] is None or self.vertex[v2] is None:
            return

        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2) -> None:

        if v1 >= self.max_vertex or v2 >= self.max_vertex:
            return

        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
