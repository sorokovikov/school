from typing import Optional, Generic, TypeVar, SupportsBytes

T = TypeVar("T", bound=SupportsBytes)


class HashTable(Generic[T]):

    REMOVE_OK = 0
    REMOVE_ERR = 1

    PUT_OK = 0
    PUT_ERR = 1

    __remove_status: int
    __put_status: int

    def __init__(self, sz: int):
        self.__size = sz
        self.__storage: list[Optional[T]] = [None] * self.__size
        self.__count = 0

    def __hash_fun(self, value: T) -> int:

        return sum(bytes(value, "utf-8")) % self.__size

    def __seek_slot(self, value: T) -> Optional[int]:

        if self.__size == self.__count:
            return None

        original_hash = self.__hash_fun(value)

        if self.__storage[original_hash] is None or self.__storage[original_hash] == value:
            return original_hash

        return None

    # запросы
    def size(self) -> int:

        return self.__count

    def find(self, value: T) -> bool:

        slot = self.__seek_slot(value)

        if slot is not None and self.__storage[slot] is None:
            result = False
        else:
            result = True
        return result

    # команды
    # предусловие: значения нет в хэш таблице
    # постусловие: значение добавляется в хэш таблицу
    def put(self, value: T) -> None:

        slot = self.__seek_slot(value)

        if slot is not None and (self.__storage[slot] is None or self.__storage[slot] != value):
            self.__storage[slot] = value
            self.__count += 1
            self.__put_status = self.PUT_OK
        else:
            self.__put_status = self.PUT_ERR

    # предусловие: значение есть в хэш таблице
    # постусловие: значение удаляется из хэш таблицы
    def remove(self, value: T) -> None:

        slot = self.__seek_slot(value)

        if slot is not None and self.__storage[slot] is not None:
            self.__storage[slot] = None
            self.__count -= 1
            self.__remove_status = self.REMOVE_OK
        else:
            self.__remove_status = self.REMOVE_ERR
