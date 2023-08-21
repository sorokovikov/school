class BloomFilter:

    def __init__(self, f_len: int):
        self.filter_len = f_len
        self.bitarray = [0] * self.filter_len
        self.filter = 0b0

    def hash1(self, str1: str) -> int:
        # 17
        code = 0
        for c in str1:
            code = ord(c) + code * 17
        return code % self.filter_len

    def hash2(self, str1: str) -> int:
        # 223
        code = 0
        for c in str1:
            code = ord(c) + code * 223
        return code % self.filter_len

    def add(self, str1: str) -> None:

        self.filter |= 0b1 << self.hash1(str1) | 0b1 << self.hash2(str1)

    def is_value(self, str1: str) -> bool:

        mask1 = 0b1 << self.hash1(str1)
        mask2 = 0b1 << self.hash2(str1)

        return self.filter | mask1 | mask2 == self.filter

    def delete(self, index: int) -> None:

        self.filter ^= 0b1 << index

