from typing import Optional


class Heap:

    def __init__(self) -> None:
        self.HeapArray: list[Optional[int]] = []

    def MakeHeap(self, a: list[int], depth: int):

        array_size = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * array_size

        for key in a:
            self.Add(key)

    def GetMax(self) -> int:

        if self.HeapArray[0] is None:
            return -1

        max_element = self.HeapArray[0]
        last_key_index = self._find_last_key_index()

        if last_key_index == 0:
            self.HeapArray[0] = None
            return max_element

        self.HeapArray[0], self.HeapArray[last_key_index] = self.HeapArray[last_key_index], None
        self._swap_with_child(0)

        return max_element

    def _find_last_key_index(self) -> int:

        for index in range(len(self.HeapArray)):
            if self.HeapArray[index] is None:
                return index - 1

        return len(self.HeapArray) - 1

    def _swap_with_child(self, root_index: int) -> None:

        if 2 * root_index + 1 >= len(self.HeapArray):
            return

        left_child_index = root_index * 2 + 1
        right_child_index = root_index * 2 + 2

        if self.HeapArray[left_child_index] is None:
            return

        max_child_index = left_child_index

        if right_child_index < len(self.HeapArray) and self.HeapArray[right_child_index] is not None:
            max_child_index = left_child_index if self.HeapArray[left_child_index] >= self.HeapArray[right_child_index] else right_child_index

        if self.HeapArray[max_child_index] > self.HeapArray[root_index]:
            self.HeapArray[root_index], self.HeapArray[max_child_index] = (
                self.HeapArray[max_child_index], self.HeapArray[root_index]
            )
            self._swap_with_child(max_child_index)

    def Add(self, key: int) -> bool:

        if self.HeapArray[len(self.HeapArray) - 1] is not None:
            return False

        first_empty_index = self._find_first_empty_index()
        self.HeapArray[first_empty_index] = key
        self._swap_with_parent(first_empty_index)
        return True

    def _find_first_empty_index(self) -> int:

        for index in range(len(self.HeapArray)):
            if self.HeapArray[index] is None:
                return index

        return -1

    def _swap_with_parent(self, child_index: int) -> None:

        parent_index = (child_index - 1) // 2

        if parent_index < 0:
            return

        if self.HeapArray[child_index] > self.HeapArray[parent_index]:
            self.HeapArray[child_index], self.HeapArray[parent_index] = (
                self.HeapArray[parent_index], self.HeapArray[child_index]
            )
            self._swap_with_parent(parent_index)
