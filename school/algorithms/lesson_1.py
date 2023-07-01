from typing import Any, Optional


class Node:

    def __init__(self, v: Any):
        self.value = v
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


class LinkedList:

    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def __eq__(self, other: Any) -> bool:

        if not isinstance(other, LinkedList):
            raise TypeError

        # if any(
        #     (
        #         self.head and not other.head,
        #         not self.head and other.head,
        #         self.tail and not other.tail,
        #         not self.tail and other.tail,
        #     )
        # ):
        #     return False
        #
        # if self.head and other.head and self.head != other.head:
        #     return False
        #
        # if self.tail and other.tail and self.tail.value != other.tail.value:
        #     return False
        if self.len() != other.len():
            return False
        if self.head != other.head:
            return False
        if self.tail != other.tail:
            return False

        for n1, n2 in zip(self, other):
            if n1 != n2:
                return False
        return True

    def __repr__(self) -> str:

        sequence = ", ".join([str(node.value) for node in self])
        return f"Head: {self.head.value if self.head else None}; " \
               f"Tail: {self.tail.value if self.tail else None}; " \
               f"Sequence: {sequence if sequence else 'None'}"

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

        prev_node = None
        node = self.head

        while node is not None:
            if node.value == val:
                if prev_node:
                    prev_node.next = node.next
                else:
                    self.head = node.next
                if node is self.tail:
                    self.tail = prev_node if prev_node else None
                if not all:
                    return
            else:
                prev_node = node
            node = node.next

        # prev_node = self.head
        # node = self.head

        # while node is not None:
        #     if node.value == val:
        #         if node is self.tail:
        #             self.tail = prev_node
        #         if node is self.head:
        #             self.head = node.next
        #             prev_node = self.head
        #             node = self.head
        #         else:
        #             prev_node.next = node.next
        #             node = node.next
        #         if not all:
        #             return
        #     else:
        #         prev_node = node
        #         node = node.next

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
            if afterNode is self.tail:
                self.tail = newNode
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
