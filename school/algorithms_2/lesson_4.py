from typing import Optional


class aBST:

    def __init__(self, depth: int):
        tree_size = 2 ** depth - 1
        self.Tree: list[Optional[int]] = [None] * tree_size

    def FindKeyIndex(self, key: int) -> Optional[int]:

        return self._find_by_key(0, key)

    def _find_by_key(self, root_index: int, key: int) -> Optional[int]:

        if root_index >= len(self.Tree):
            return None

        if self.Tree[root_index] is None:
            return root_index * -1

        if key < self.Tree[root_index]:
            return self._find_by_key(root_index=(root_index * 2 + 1), key=key)

        if key > self.Tree[root_index]:
            return self._find_by_key(root_index=(root_index * 2 + 2), key=key)

        return root_index

    def AddKey(self, key: int) -> int:

        index = self.FindKeyIndex(key)

        if index is None:
            return -1

        if index <= 0:
            index *= -1
            self.Tree[index] = key
            return index

        return index
