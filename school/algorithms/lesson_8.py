from typing import Optional


class HashTable:

    def __init__(self, sz: int, stp: int):
        self.size = sz
        self.step = stp
        self.slots: list[Optional[str]] = [None] * self.size

    def hash_fun(self, value: str) -> int:

        return sum(bytes(value, "utf-8")) % self.size

    def seek_slot(self, value: str) -> Optional[int]:

        if self.size == len([v for v in self.slots if v is not None]):
            return None

        original_hash = self.hash_fun(value)

        if self.slots[original_hash] is None:
            return original_hash

        if self.slots[original_hash] == value:
            return original_hash

        slot = None
        hash = original_hash
        while hash < self.size:
            hash += self.step
            if self.slots[hash] is None:
                return hash

        hash = 0
        while hash < original_hash:
            hash += self.step
            if self.slots[hash] is None:
                return hash
        return None

    def put(self, value: str) -> Optional[int]:

        slot = self.seek_slot(value)
        if slot is None:
            return None

        self.slots[slot] = value
        return slot

    def find(self, value: str) -> Optional[int]:

        # try:
        #     return self.slots.index(value)
        # except ValueError:
        #     return None

        hash = self.hash_fun(value)
        if self.slots[hash] is None:
            return None
        return hash