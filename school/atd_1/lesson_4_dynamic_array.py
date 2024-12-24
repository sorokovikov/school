import ctypes
from typing import Generic, TypeVar

T = TypeVar("T")


class DynArray(Generic[T]):

    GET_ITEM_OK = 1
    GET_ITEM_ERR = 2

    INSERT_OK = 1
    INSERT_ERR = 2

    REMOVE_OK = 1
    REMOVE_ERR = 2

    __get_item_status: int
    __insert_status: int
    __remove_status: int

    # конструктор
    # постусловие: создаётся новый объект пустого динамического массива
    def __init__(self):

        self.count = 0
        self.capacity = 16
        self.array = self.__make_array(self.capacity)

    # запросы:
    # предусловие: элемент массива по запрашиваемому индексу существует
    def get_item(self, i: int) -> T:

        if i < 0 or i >= self.count:
            self.__get_item_status = self.GET_ITEM_ERR
            return

        self.__get_item_status = self.GET_ITEM_OK
        return self.array[i]

    # команды:
    # постусловие: в конец массива добавляется новый элемент
    def append(self, itm: T) -> None:

        if self.count == self.capacity:
            self.__resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    # предусловие: переданный индекс не превышает кол-во элементов массива и не ниже 0
    # постусловие: в переданный индекс вставляется новый элемент, элементы справа смещаются
    def insert(self, i: int, itm: T) -> None:

        if i < 0 or i > self.count:
            self.__insert_status = self.INSERT_ERR
            return

        if self.count == self.capacity:
            self.__resize(2 * self.capacity)

        for j in range(self.count, i, -1):
            self.array[j] = self.array[j - 1]
        self.array[i] = itm
        self.count += 1

        self.__insert_status = self.INSERT_OK

    # предусловие: по запрашиваемому индексу существует элемент
    # постусловие: элемент удаляется из массива
    def remove(self, i: int) -> None:

        if i < 0 or i >= self.count:
            self.__remove_status = self.REMOVE_ERR
            return

        for j in range(i, self.count - 1):
            self.array[j] = self.array[j + 1]

        self.count -= 1
        new_capacity = int(self.capacity / 1.5)
        need_resize = self.count < int(self.capacity / 2)
        if need_resize and new_capacity > 16:
            self.__resize(new_capacity)
        if need_resize and new_capacity <= 16 and self.capacity != 16:
            self.__resize(16)

        self.__remove_status = self.REMOVE_OK

    def __resize(self, new_capacity: int):

        new_array = self.__make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def __make_array(self, new_capacity: int):

        return (new_capacity * ctypes.py_object)()

    # запросы статусов
    def get_get_item_status(self) -> int:

        return self.__get_item_status

    def get_insert_status(self) -> int:

        return self.__insert_status

    def get_remove_status(self) -> int:

        return self.__remove_status
