class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bitarray = [0] * self.filter_len

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

        self.bitarray[self.hash1(str1)] = 1
        self.bitarray[self.hash2(str1)] = 1

    def is_value(self, str1: str) -> bool:

        if self.bitarray[self.hash1(str1)] == 1:
            return True
        if self.bitarray[self.hash2(str1)] == 1:
            return True
        return False

    def delete(self, index: int) -> None:

        self.bitarray[index] = 0
