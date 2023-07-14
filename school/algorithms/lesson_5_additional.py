from typing import Any, Optional, Union

from algorithms.lesson_5 import Queue


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

    def get_head(self) -> Optional[Node]:

        return self.head if self.head is not None else None

    def add_in_head(self, item: Node) -> None:

        if self.tail is None:
            self.tail = item
        item.next = self.head
        self.head = item
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


class Stack:

    def __init__(self) -> None:
        self.stack = LinkedList()

    def size(self) -> int:

        return self.stack.count

    def pop(self) -> Optional[Any]:

        if self.size() == 0:
            return None
        return self.stack.pop_head().value

    def push(self, value: Any) -> None:

        self.stack.add_in_head(Node(value))

    def peek(self) -> Optional[Any]:

        if self.size() == 0:
            return None
        head = self.stack.get_head()
        return head.value

    def get_values(self) -> list[Any]:

        return self.stack.get_nodes_values()


class QueueWithStacks:

    def __init__(self) -> None:

        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item: Any) -> None:

        self.stack1.push(item)

    def dequeue(self) -> Optional[Any]:

        if self.stack1.size() == 0 and self.stack2.size() == 0:
            return None

        if self.stack2.size() == 0:
            while self.stack1.size() > 0:
                self.stack2.push(self.stack1.pop())

        return self.stack2.pop()

    def size(self) -> int:

        return self.stack1.size() + self.stack2.size()

    def get_values(self) -> list[Any]:

        if self.stack1.size() == 0 and self.stack2.size() == 0:
            return []

        result = self.stack2.get_values()
        result.extend(reversed(self.stack1.get_values()))
        return result


def rotate_queue(q: Union[Queue, QueueWithStacks], rotation: int) -> None:

    for _ in range(rotation):
        q.enqueue(q.dequeue())



