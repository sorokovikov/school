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
