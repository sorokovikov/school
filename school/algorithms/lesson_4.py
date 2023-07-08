import ctypes
from typing import Any, Optional


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity: int):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i: int):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity: int):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm: Any):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def delete(self, i: int):

        # check if `i` is within bounds
        _ = self[i]

        for j in range(i, self.count - 1):
            self.array[j] = self.array[j + 1]

        self.count -= 1
        new_capacity = int(self.capacity / 1.5)
        need_resize = self.count < int(self.capacity / 2)
        if need_resize and new_capacity > 16:
            self.resize(new_capacity)
        if need_resize and new_capacity <= 16 and self.capacity != 16:
            self.resize(16)

    def get_values(self) -> list:

        return [self.array[i] for i in range(self.count)]


class Stack:
    def __init__(self) -> None:
        self.stack = DynArray()

    def size(self) -> int:

        return self.stack.count

    def pop(self) -> Optional[Any]:

        if self.stack.count == 0:
            return None
        value = self.stack[self.stack.count - 1]
        self.stack.delete(self.stack.count - 1)
        return value

    def push(self, value: Any) -> None:

        self.stack.append(value)

    def peek(self) -> Optional[Any]:

        if self.stack.count == 0:
            return None
        return self.stack[self.stack.count - 1]

    def get_values(self) -> list[Any]:

        return self.stack.get_values()
