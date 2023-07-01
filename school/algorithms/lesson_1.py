from typing import Any, Optional


class Node:

    def __init__(self, v: Any):
        self.value = v
        self.next: Optional[Node] = None


class LinkedList:

    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def __eq__(self, other: Any) -> bool:

        if not isinstance(other, LinkedList):
            raise TypeError

        for n1, n2 in zip(self, other):
            if n1.value != n2.value:
                return False
        return True

    def __iter__(self):

        return LinkedListIterator(self)

    def add_in_start(self, item: Node) -> None:

        if self.tail is None:
            self.tail = item
        item.next = self.head
        self.head = item

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val: Any) -> list[Node]:

        result: list[Node] = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next

        return result

    def delete(self, val: Any, all: bool = False) -> None:

        if self.head is None:
            return

        prev_node = self.head
        node = self.head

        while node is not None:
            if node.value == val:
                if node is self.head:
                    self.head = node.next
                    prev_node = self.head
                    node = self.head
                else:
                    prev_node.next = node.next
                    node = node.next

                if not all:
                    return
            else:
                prev_node = node
                node = node.next

    def clean(self) -> None:

        self.head = None
        self.tail = None

    def len(self) -> int:

        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next

        return count

    def insert(self, afterNode: Optional[Node], newNode: Node) -> None:

        if afterNode is None:
            self.add_in_start(newNode)
        else:
            newNode.next, afterNode.next = afterNode.next, newNode


class LinkedListIterator:

    def __init__(self, linked_list: LinkedList):
        self.__linked_list = linked_list
        self.__current_node = self.__linked_list.head

    def __next__(self):

        if self.__current_node is not None:
            node = self.__current_node
            self.__current_node = self.__current_node.next
            return node

        raise StopIteration
