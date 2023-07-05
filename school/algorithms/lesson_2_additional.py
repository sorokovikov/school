from typing import Any, Optional


class Node:
    def __init__(self, v):
        self.value = v
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None

    def __eq__(self, other: Any):

        if other and not isinstance(other, Node):
            raise TypeError

        if self is None and other is not None:
            return False
        if self is not None and other is None:
            return False
        if self and other and self.value != other.value:
            return False
        return True


class LinkedListDummyNodes:
    def __init__(self):
        self.head: Node = Node(None)
        self.tail: Node = Node(None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def __repr__(self) -> str:

        sequence = ", ".join([str(node.value) for node in self])
        return f"Head: {self.head.next.value if self.head.next else None}; " \
               f"Tail: {self.tail.prev.value if self.tail.prev else None}; " \
               f"Len: {self.len()}; " \
               f"Sequence: {sequence if sequence else 'None'}"

    def __iter__(self):

        return LinkedListDummyNodesIterator(self)

    def __eq__(self, other: Any) -> bool:

        if not isinstance(other, LinkedListDummyNodes):
            raise TypeError

        if self.len() != other.len():
            return False

        for n1, n2 in zip(self, other):
            if n1 != n2:
                return False
        return True

    def print_all(self) -> None:

        for node in self:
            print(node.value)

    def add_in_tail(self, item: Node) -> None:
        """Adds node in tail"""

        item.prev = self.tail.prev
        item.prev.next = item
        item.next = self.tail
        item.next.prev = item

    def add_in_head(self, item: Node) -> None:
        """Adds node in head"""

        item.next = self.head.next
        item.next.prev = item
        item.prev = self.head
        item.prev.next = item

    def find(self, val: Any) -> Optional[Node]:
        """Finds node by value"""

        node = self.head.next
        while node is not self.tail:
            if node.value == val:
                return node
            node = node.next

        return None

    def find_all(self, val: Any) -> list[Node]:
        """Finds all nodes in linked list which values equals passed value"""

        result: list[Node] = []
        node = self.head.next
        while node is not self.tail:
            if node.value == val:
                result.append(node)
            node = node.next

        return result

    def delete(self, val: Any, all: bool = False) -> None:
        """
        If argument `all` is True, then deletes all nodes which value equals passed value.
        Otherwise - deletes only one node.
        """

        if self.len() == 0:
            return

        node = self.head.next
        while node is not self.tail:
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                if not all:
                    return
            node = node.next

    def clean(self) -> None:

        self.head = Node(None)
        self.tail = Node(None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def len(self) -> int:

        count = 0
        node = self.head.next
        while node is not self.tail:
            count += 1
            node = node.next

        return count

    def insert(self, afterNode: Optional[Node], newNode: Node) -> None:

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


class LinkedListDummyNodesIterator:

    def __init__(self, linked_list: LinkedListDummyNodes):
        self.__linked_list = linked_list
        self.__current_node = self.__linked_list.head.next

    def __next__(self):

        if self.__current_node is not self.__linked_list.tail:
            node = self.__current_node
            self.__current_node = self.__current_node.next
            return node

        raise StopIteration


class LinkedListDummyNode:

    def __init__(self):
        self.dummy_node = Node(None)
        self.dummy_node.next = self.dummy_node
        self.dummy_node.prev = self.dummy_node

    def print_all(self):

        node = self.dummy_node.next
        while node is not self.dummy_node:
            print(node.value)
            node = node.next

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
