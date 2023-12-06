from functools import reduce
from typing import Any, Optional


class Node:
    def __init__(self, v):
        self.value = v
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None

    def __eq__(self, other: Any) -> bool:

        if not isinstance(other, Node):
            raise TypeError

        if self.value != other.value:
            return False
        return True


class LinkedList:

    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.count = 0

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        self.count += 1

    def pop_head(self) -> Optional[Node]:

        if self.count == 0:
            return None
        value = self.head
        self.head = self.head.next
        self.count -= 1
        return value

    def get_nodes_values(self) -> list[Any]:

        result = []
        node = self.head
        while node is not None:
            result.append(node.value)
            node = node.next

        return result


class Queue:

    def __init__(self) -> None:

        self.queue = LinkedList()

    def enqueue(self, item: Any) -> None:

        self.queue.add_in_tail(Node(item))

    def dequeue(self) -> Optional[Any]:

        if self.queue.count == 0:
            return None
        return self.queue.pop_head().value

    def size(self) -> int:

        return self.queue.count

    def get_values(self) -> list[Any]:

        return self.queue.get_nodes_values()


class Vertex:

    def __init__(self, val: int):
        self.Value = val
        self.Hit = False

    def visit(self) -> None:

        self.Hit = True

    def is_visited(self):

        return self.Hit


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

    def DepthFirstSearch(self, VFrom: int, VTo: int) -> list[Vertex]:

        self.__reset_vertices()

        if (
            not (0 <= VFrom < self.max_vertex - 1) or
            not (0 <= VTo < self.max_vertex - 1) or
            self.vertex[VFrom] is None or self.vertex[VTo] is None
        ):
            return []

        stack: list[Vertex] = []
        self.__depth_first_search(VFrom, VTo, stack)
        return stack

    def __depth_first_search(self, v_from: int, v_to: int, stack: list[Vertex]) -> list[Vertex]:

        self.vertex[v_from].visit()
        stack.append(self.vertex[v_from])

        if self.IsEdge(v_from, v_to):
            self.vertex[v_to].visit()
            stack.append(self.vertex[v_to])
            return stack

        for adjacent_vertex in self.__get_adjacent_vertices(v_from):
            if not self.vertex[adjacent_vertex].is_visited():
                return self.__depth_first_search(adjacent_vertex, v_to, stack)

        stack.pop()

        if len(stack) == 0:
            return []

        last_vertex_index = self.vertex.index(stack[-1])
        stack.pop()
        return self.__depth_first_search(last_vertex_index, v_to, stack)

    def __get_adjacent_vertices(self, parent_vertex: int) -> list[int]:

        adjacent_vertices: list[int] = []

        for i in range(self.max_vertex):
            if self.IsEdge(parent_vertex, i):
                adjacent_vertices.append(i)
        return adjacent_vertices

    def __reset_vertices(self) -> None:

        for vertex in self.vertex:
            if vertex is not None:
                vertex.Hit = False

    def BreadthFirstSearch(self, VFrom: int, VTo: int) -> list[Vertex]:

        self.__reset_vertices()
        if (
            not (0 <= VFrom <= self.max_vertex - 1) or
            not (0 <= VTo <= self.max_vertex - 1) or
            self.vertex[VFrom] is None or self.vertex[VTo] is None
        ):
            return []

        queue = Queue()
        self.vertex[VFrom].visit()
        path_history: list[Optional[int]] = [None] * self.max_vertex * self.max_vertex

        def find_path(v_from: int):

            for adjacent_vertex in self.__get_adjacent_vertices(v_from):
                if not self.vertex[adjacent_vertex].is_visited():
                    if adjacent_vertex == VTo:
                        path_history[adjacent_vertex] = v_from
                        return
                    self.vertex[adjacent_vertex].visit()
                    queue.enqueue(adjacent_vertex)
                    path_history[adjacent_vertex] = v_from

            if queue.size() == 0:
                path_history.clear()
                return

            find_path(queue.dequeue())

        find_path(VFrom)

        if len(path_history) == 0:
            return []

        path = []
        current = VTo
        path.append(self.vertex[current])

        while current != VFrom:
            current = path_history[current]
            path.append(self.vertex[current])

        path.reverse()
        return path
