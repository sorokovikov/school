from typing import Any, Optional


class Node:

    def __init__(self, v: Any):
        self.value = v
        self.next: Optional[Node] = None


class LinkedList:

    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def __iter__(self):

        return LinkedListIterator(self)

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

    def find_all(self, val: Any):

        result: list[Node] = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next

        return result

    def delete(self, val: Any, all: bool = False):

        if self.head is None:
            return

        prev_node = self.head
        while prev_node.next is not None:
            node = prev_node.next
            if prev_node.next.value == val:
                prev_node.next = node.next
                if not all:
                    return
            prev_node = node

    def clean(self):

        self.head = None
        self.tail = None

    def len(self):

        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next

        return count

    def insert(self, afterNode: Optional[Node], newNode: Node):

        if afterNode is None:
            newNode.next, self.head = self.head, newNode
            # newNode.next = self.head
            # self.head = newNode
        else:
            newNode.next, afterNode.next = afterNode.next, newNode
            # newNode.next = afterNode.next
            # afterNode.next = newNode


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


def sum_nodes(n1: Node, n2: Node) -> Node:

    return Node(n1.value + n2.value)


def sum_linked_lists(ll1: LinkedList, ll2: LinkedList) -> Optional[LinkedList]:

    if ll1.len() != ll2.len():
        return None
    result = LinkedList()

    for n1, n2 in zip(ll1, ll2):
        result.add_in_tail(sum_nodes(n1, n2))
    return result
