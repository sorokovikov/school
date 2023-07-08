from algorithms.lesson_4 import Stack


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
