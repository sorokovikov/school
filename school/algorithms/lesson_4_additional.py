from typing import Any, Optional

from algorithms.lesson_4 import Stack
from algorithms.lesson_2_additional import LinkedListDummyNode, Node


class StackHead:

    def __init__(self) -> None:
        self.stack = LinkedListDummyNode()

    def size(self) -> int:

        return self.stack.len()

    def pop(self) -> Optional[Any]:

        head = self.stack.get_head()
        if self.size() == 0 or head is None:
            return None
        self.stack.delete(head.value)
        return head.value

    def push(self, value: Any) -> None:

        self.stack.add_in_head(Node(value))

    def peek(self) -> Optional[Any]:

        head = self.stack.get_head()
        if self.size() == 0 or head is None:
            return None
        return head.value

    def get_values(self) -> list[Any]:

        return self.stack.get_nodes_values()


def check_parentheses(string: str) -> bool:

    stack = Stack()
    for char in string:
        stack.push(char)

    char = stack.pop()
    if char == "(":
        return False

    count = 1
    while char is not None:
        char = stack.pop()
        if char == "(":
            count -= 1
        if char == ")":
            count += 1

        if count < 0:
            return False

    if count == 0:
        return True
    return False


def calculate_postfix_notation(s1: StackHead) -> Optional[int]:

    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }
    s2 = StackHead()

    while s1.size() > 0:
        elem: str = s1.pop()
        try:
            s2.push(int(elem))
        except ValueError:
            if elem in ("+", "*"):
                s2.push(operations.get(elem)(s2.pop(), s2.pop()))
            if elem == "=":
                return s2.pop()
    return None


def convert_postfix_notation_to_stack(s: str) -> StackHead:

    stack = StackHead()
    for char in reversed(s.split(" ")):
        stack.push(char)
    return stack
