from itertools import zip_longest
from typing import Any, Optional


class Node:

    def __init__(self, v: Any):
        self.value = v
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class OrderedList:

    def __init__(self, asc: bool):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.__ascending = asc
        self.__count = 0

    def compare(self, v1: Any, v2: Any) -> int:

        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
        return 0

    def add(self, value: Any) -> None:

        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            self.__count += 1
            return

        new_node = Node(value)
        node = self.head
        while node is not None:
            compare_result = self.compare(node.value, value)

            if (
                ((compare_result == -1 and self.__ascending) or (compare_result == 1 and not self.__ascending))
                and node is self.tail
            ):
                new_node.prev = node
                new_node.prev.next = new_node
                self.tail = new_node
                self.__count += 1
                return

            if compare_result in (0, 1) and self.__ascending or compare_result in (-1, 0) and not self.__ascending:
                new_node.next = node
                new_node.prev = node.prev
                new_node.next.prev = new_node
                if node is self.head:
                    self.head = new_node
                else:
                    new_node.prev.next = new_node
                self.__count += 1
                return

            node = node.next

    def find(self, val: Any) -> Optional[Node]:

        if self.len() == 0:
            return None

        node = self.head
        while node is not None:
            compare_result = self.compare(node.value, val)
            if compare_result == 1 and self.__ascending or compare_result == -1 and not self.__ascending:
                return None
            if compare_result == 0:
                return node
            node = node.next
        return None

    def delete(self, val: Any) -> None:

        node = self.find(val)

        if node is None:
            return

        if self.len() == 1:
            self.clean(self.__ascending)
            return

        if node is not self.head and node is not self.tail:
            node.prev.next = node.next
            node.next.prev = node.prev
        if node is self.head:
            node.next.prev = None
            self.head = node.next
        if node is self.tail:
            node.prev.next = None
            self.tail = node.prev

        self.__count -= 1

    def clean(self, asc: bool) -> None:

        self.__ascending = asc
        self.head = None
        self.tail = None
        self.__count = 0

    def len(self: Any) -> int:

        return self.__count

    def get_all(self) -> list[Node]:
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

    def get_nodes_values(self) -> list[Any]:

        return [n.value for n in self.get_all()]


class OrderedStringList(OrderedList):

    def __init__(self, asc: bool):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1: str, v2: str) -> int:
        stripped_v1 = v1.lstrip().rstrip()
        stripped_v2 = v2.lstrip().rstrip()

        for char_1, char_2 in zip_longest(stripped_v1, stripped_v2):
            if char_1 is None:
                return -1
            if char_2 is None:
                return 1
            char_1_ord = ord(char_1)
            char_2_ord = ord(char_2)
            compare_result = super().compare(char_1_ord, char_2_ord)
            if compare_result == 0:
                continue
            return compare_result
        return 0
