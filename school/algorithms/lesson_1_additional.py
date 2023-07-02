from typing import Optional

from algorithms.lesson_1 import LinkedList, Node


def sum_nodes(n1: Node, n2: Node) -> Node:

    return Node(n1.value + n2.value)


def sum_linked_lists(ll1: LinkedList, ll2: LinkedList) -> Optional[LinkedList]:

    if ll1.len() != ll2.len():
        return None
    result = LinkedList()

    for n1, n2 in zip(ll1, ll2):
        result.add_in_tail(sum_nodes(n1, n2))
    return result
