from typing import Optional


class HashTable:

    def __init__(self, sz: int, stp: int):
        self.size = sz
        self.step = stp
        self.slots: list[Optional[str]] = [None] * self.size
        self.count = 0

    def hash_fun(self, value: str) -> int:

        return sum(bytes(value, "utf-8")) % self.size

    def seek_slot(self, value: str) -> Optional[int]:

        if self.size == self.count:
            return None

        original_hash = self.hash_fun(value)

        if self.slots[original_hash] is None or self.slots[original_hash] == value:
            return original_hash

        dif_hash = original_hash

        while dif_hash < self.size:
            if self.slots[dif_hash] is None or self.slots[original_hash] == value:
                return dif_hash
            dif_hash += self.step

        dif_hash = dif_hash - self.size
        while dif_hash < original_hash:
            if self.slots[dif_hash] is None or self.slots[original_hash] == value:
                return dif_hash
            dif_hash += self.step
            # if dif_hash >= self.size:
            #     dif_hash -= self.size
        return None

    def put(self, value: str) -> Optional[int]:

        slot = self.seek_slot(value)
        if slot is None:
            return None
        if self.slots[slot] is None or self.slots[slot] != value:
            self.slots[slot] = value
            self.count += 1
        return slot

    def find(self, value: str) -> Optional[int]:

        original_hash = self.hash_fun(value)
        dif_hash = original_hash
        while dif_hash < self.size:
            if self.slots[dif_hash] is None:
                return None
            if self.slots[dif_hash] == value:
                return dif_hash
            dif_hash += self.step

        dif_hash -= self.size
        while dif_hash < original_hash:
            if self.slots[dif_hash] is None:
                return None
            if self.slots[dif_hash] == value:
                return dif_hash
            dif_hash += self.step
        return None
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        # hash = original_hash + self.step
        # while hash < self.size:
        #     if self.slots[hash] is None:
        #         return None
        #     if self.slots[hash] == value:
        #         return hash
        #     hash += self.step
        #
        # hash = 0
        # while hash < original_hash:
        #     if self.slots[hash] is None:
        #         return None
        #     if self.slots[hash] == value:
        #         return hash
        #     hash += self.step
        # return None
