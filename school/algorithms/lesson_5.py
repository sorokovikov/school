from typing import Any, Optional


class Node:
    def __init__(self, v):
        self.value = v
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None

    def __eq__(self, other: Any):

        if not isinstance(other, Node):
            raise TypeError

        if self.value != other.value:
            return False
        return True


class LinkedListDummyNode:

    def __init__(self):
        self.dummy_node = Node(None)
        self.dummy_node.next = self.dummy_node
        self.dummy_node.prev = self.dummy_node

    def get_head(self) -> Optional[Node]:

        return self.dummy_node.next if self.dummy_node.next is not self.dummy_node else None

    def add_in_head(self, newNode: Node):

        newNode.next = self.dummy_node.next
        newNode.next.prev = newNode
        newNode.prev = self.dummy_node
        newNode.prev.next = newNode

    def add_in_tail(self, item: Node):

        item.prev = self.dummy_node.prev
        item.prev.next = item
        item.next = self.dummy_node
        item.next.prev = item

    def find(self, val: Any):

        node = self.dummy_node.next
        while node is not self.dummy_node:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val: Any):

        result: list[Node] = []
        node = self.dummy_node.next
        while node is not self.dummy_node:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val: Any, all: bool = False) -> None:

        if self.len() == 0:
            return

        node = self.dummy_node.next
        while node is not self.dummy_node:
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                if not all:
                    return
            node = node.next

    def clean(self):

        self.dummy_node = Node(None)
        self.dummy_node.next = self.dummy_node
        self.dummy_node.prev = self.dummy_node

    def len(self):

        count = 0
        node = self.dummy_node.next
        while node is not self.dummy_node:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode: Node, newNode: Node):

        length = self.len()

        if afterNode is None and length == 0:
            self.add_in_head(newNode)
        if afterNode is None and length > 0:
            self.add_in_tail(newNode)
        if afterNode:
            newNode.prev = afterNode
            newNode.next = afterNode.next
            afterNode.next.prev = newNode
            afterNode.next = newNode

    def get_nodes_values(self) -> list[Any]:

        result = []
        node = self.dummy_node.next
        while node is not self.dummy_node:
            result.append(node.value)
            node = node.next
        return result


class Queue:

    def __init__(self) -> None:

        self.queue = LinkedListDummyNode()

    def enqueue(self, item: Any) -> None:

        self.queue.add_in_tail(Node(item))

    def dequeue(self) -> Optional[Any]:

        head = self.queue.get_head()
        if self.size() == 0 or head is None:
            return None
        self.queue.delete(head.value)
        return head.value

    def size(self) -> int:

        return self.queue.len()

    def get_values(self) -> list[Any]:

        return self.queue.get_nodes_values()
