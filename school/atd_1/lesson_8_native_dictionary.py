from typing import Any, Generic, Optional, TypeVar

T = TypeVar("T")


class NativeDictionary(Generic[T]):

    GET_OK = 0
    GET_ERR = 1

    PUT_OK = 0
    PUT_ERR = 1

    __get_status: int
    __put_status: int

    def __init__(self, sz: int):

        self.size = sz
        self.slots: list[Optional[str]] = [None] * self.size
        self.values: list[Optional[T]] = [None] * self.size
        self.count = 0

    def __hash_fun(self, key: str) -> int:

        return sum(bytes(key, "utf-8")) % self.size

    def __seek_slot(self, key: str) -> Optional[int]:

        if self.size == self.count:
            return None

        original_hash = self.__hash_fun(key)

        for dif_hash in range(original_hash, self.size):
            if self.slots[dif_hash] is None or self.slots[dif_hash] == key:
                return dif_hash

        for dif_hash in range(original_hash):
            if self.slots[dif_hash] is None or self.slots[dif_hash] == key:
                return dif_hash
        return None

    # запросы
    # предусловие: в словаре есть значение по запрашиваемому ключу
    def get(self, key: str) -> Optional[T]:

        original_hash = self.__hash_fun(key)

        for dif_hash in range(original_hash, self.size):
            if self.slots[dif_hash] is None:
                self.__get_status = self.GET_ERR
                return None
            if self.slots[dif_hash] == key:
                self.__get_status = self.GET_OK
                return self.values[dif_hash]

        for dif_hash in range(original_hash):
            if self.slots[dif_hash] is None:
                self.__get_status = self.GET_ERR
                return None
            if self.slots[dif_hash] == key:
                self.__get_status = self.GET_OK
                return self.values[dif_hash]

        self.__get_status = self.GET_ERR
        return None

    def is_key(self, key: str) -> bool:

        original_hash = self.__hash_fun(key)

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

    def get_get_status(self) -> int:

        return self.__get_status

    def get_put_status(self) -> int:

        return self.__put_status

    # команды
    # предусловие: в словаре есть свободный слот
    # постусловие: в словарь добавляется пара ключ-значение
    def put(self, key: str, value: T) -> None:

        slot = self.__seek_slot(key)
        if slot is None:
            self.__put_status = self.PUT_ERR
            return
        self.slots[slot] = key
        self.values[slot] = value
        self.count += 1
        self.__put_status = self.PUT_ok
