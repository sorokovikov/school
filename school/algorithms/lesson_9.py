from typing import Any, Optional


class NativeDictionary:

    def __init__(self, sz: int):

        self.size = sz
        self.slots: list[Optional[str]] = [None] * self.size
        self.values: list[Optional[Any]] = [None] * self.size
        self.count = 0

    def hash_fun(self, key: str) -> int:

        return sum(bytes(key, "utf-8")) % self.size

    def is_key(self, key: str) -> bool:

        original_hash = self.hash_fun(key)

        for dif_hash in range(original_hash, self.size):
            if self.slots[dif_hash] is None:
                return False
            if self.slots[dif_hash] == key:
                return True

        for dif_hash in range(original_hash):
            if self.slots[dif_hash] is None:
                return False
            if self.slots[dif_hash] == key:
                return True

        return False

    def seek_slot(self, key: str) -> Optional[int]:

        if self.size == self.count:
            return None

        original_hash = self.hash_fun(key)

        for dif_hash in range(original_hash, self.size):
            if self.slots[dif_hash] is None or self.slots[dif_hash] == key:
                return dif_hash

        for dif_hash in range(original_hash):
            if self.slots[dif_hash] is None or self.slots[dif_hash] == key:
                return dif_hash
        return None

    def put(self, key: str, value: Any) -> None:

        slot = self.seek_slot(key)
        if slot is None:
            return
        self.slots[slot] = key
        self.values[slot] = value
        self.count += 1

    def get(self, key: str) -> Optional[Any]:

        original_hash = self.hash_fun(key)

        for dif_hash in range(original_hash, self.size):
            if self.slots[dif_hash] is None:
                return None
            if self.slots[dif_hash] == key:
                return self.values[dif_hash]

        for dif_hash in range(original_hash):
            if self.slots[dif_hash] is None:
                return None
            if self.slots[dif_hash] == key:
                return self.values[dif_hash]

        return None
