from typing import Any, Optional


class Node:
    def __init__(self, v):
        self.value = v
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class LinkedListDummyNode:

    def __init__(self) -> None:
        self.dummy_node = Node(None)
        self.dummy_node.next = self.dummy_node
        self.dummy_node.prev = self.dummy_node
        self.count = 0

    def get_head(self) -> Optional[Node]:

        return self.dummy_node.next if self.dummy_node.next is not self.dummy_node else None

    def add_in_head(self, newNode: Node) -> None:

        newNode.next = self.dummy_node.next
        newNode.next.prev = newNode
        newNode.prev = self.dummy_node
        newNode.prev.next = newNode
        self.count += 1

    def add_in_tail(self, item: Node) -> None:

        item.prev = self.dummy_node.prev
        item.prev.next = item
        item.next = self.dummy_node
        item.next.prev = item
        self.count += 1

    def remove_head(self) -> Optional[Node]:

        if self.len() == 0:
            return
        node = self.dummy_node.next
        self.dummy_node.next.next.prev = self.dummy_node
        self.dummy_node.next = self.dummy_node.next.next
        self.count -= 1
        return node

    def remove_tail(self) -> Optional[Node]:

        if self.len() == 0:
            return
        node = self.dummy_node.prev
        self.dummy_node.prev.prev.next = self.dummy_node
        self.dummy_node.prev = self.dummy_node.prev.prev
        self.count -= 1
        return node

    def len(self) -> int:

        return self.count

    def get_nodes_values(self) -> list[Any]:

        result = []
        node = self.dummy_node.next
        while node is not self.dummy_node:
            result.append(node.value)
            node = node.next
        return result


class Deque:
    def __init__(self) -> None:

        self.deque = LinkedListDummyNode()

    def addFront(self, item: Any) -> None:

        self.deque.add_in_head(Node(item))

    def addTail(self, item: Any) -> None:

        self.deque.add_in_tail(Node(item))

    def removeFront(self) -> Optional[Any]:

        if node := self.deque.remove_head():
            return node.value
        return None

    def removeTail(self) -> Optional[Any]:

        if node := self.deque.remove_tail():
            return node.value
        return None

    def size(self) -> int:

        return self.deque.len()

    def get_values(self) -> list[Any]:

        return self.deque.get_nodes_values()
