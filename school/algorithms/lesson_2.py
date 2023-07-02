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


class LinkedList2:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def __eq__(self, other: Any) -> bool:

        if not isinstance(other, LinkedList2):
            raise TypeError

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

        return LinkedList2Iterator(self)

    def add_in_tail(self, item: Node) -> None:
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val: Any) -> Optional[Node]:

        # go from head
        # node = self.head
        # while node is not None:
        #     if node.value == val:
        #         return node
        #     node = node.next

        # go from tail
        node = self.tail
        while node is not None:
            if node.value == val:
                return node
            node = node.prev
        return None

    def find_all(self, val: Any) -> list[Node]:

        # go from head
        # result: list[Node] = []
        # node = self.head
        # while node is not None:
        #     if node.value == val:
        #         result.append(node)
        #     node = node.next

        # go from tail
        result: list[Node] = []
        node = self.tail
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.prev
        return result

    def delete(self, val: Any, all: bool = False) -> None:

        if self.len() == 0:
            return

        node = self.head
        while node is not None:
            if node.value == val:
                # if node is self.head:
                #     if node.next:
                #         node.next.prev = None
                #     self.head = node.next
                #
                # else:
                if node.prev:
                    node.prev.next = node.next
                else:
                    if node.next:
                        node.next.prev = None
                    self.head = node.next
                if node.next:
                    node.next.prev = node.prev
                else:
                    if node.prev: # -> 3
                        node.prev.next = None
                    self.tail = node.prev

                # correct
                # if node is self.tail:
                #     if node.prev:
                #         node.prev.next = None
                #     self.tail = node.prev

                if not all:
                    return
            node = node.next

    def clean(self) -> None:

        self.head = None
        self.tail = None

    def len(self) -> int:

        # go from head
        # count = 0
        # node = self.head
        # while node is not None:
        #     count += 1
        #     node = node.next

        # go from tail
        count = 0
        node = self.tail
        while node is not None:
            count += 1
            node = node.prev
        return count

    def insert(self, afterNode: Optional[Node], newNode: Node) -> None:

        if afterNode is None:
            if self.len() == 0:
                self.add_in_head(newNode)
            else:
                self.add_in_tail(newNode)
        else:
            newNode.prev = afterNode
            newNode.next = afterNode.next
            afterNode.next.prev = newNode
            afterNode.next = newNode

    def add_in_head(self, newNode: Node) -> None:

        if self.tail is None:
            self.tail = newNode
        newNode.next = self.head
        newNode.prev = None
        self.head = newNode


class LinkedList2Iterator:

    def __init__(self, linked_list: LinkedList2):
        self.__linked_list = linked_list
        self.__current_node = self.__linked_list.head

    def __next__(self):

        if self.__current_node is not None:
            node = self.__current_node
            self.__current_node = self.__current_node.next
            return node

        raise StopIteration
