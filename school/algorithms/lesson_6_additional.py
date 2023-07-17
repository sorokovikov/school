from algorithms.lesson_6 import Deque


def is_palindrome(string: str) -> bool:

    d = Deque()
    for char in string:
        d.addTail(char)

    while d.size() > 1:
        if d.removeFront() != d.removeTail():
            return False
    return True
