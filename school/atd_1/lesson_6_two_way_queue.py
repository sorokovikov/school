from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class ParentQueue(Generic[T]):

    GET_FRONT_OK = 0
    GET_FRONT_ERR = 1

    REMOVE_FRONT_OK = 0
    REMOVE_FRONT_ERR = 1

    __get_front_status: int
    __remove_front_status: int

    # конструктор
    # постусловие: создан новый объект пустой очереди
    def __init__(self):

        self.__queue: list[T] = []

    # запросы
    def size(self) -> int:

        return len(self.__queue)

    def get_get_front_status(self) -> int:

        return self.__get_front_status

    def get_remove_front_status(self) -> int:

        return self.__remove_front_status

    # предусловие: очередь непустая
    def get_front(self) -> T:

        if self.size() > 0:
            result = self.__queue[0]
            self.__get_front_status = self.GET_FRONT_OK
        else:
            result = 0
            self.__get_front_status = self.GET_FRONT_ERR
        return result

    # команды
    # постусловие: в конец очереди добавлен элемент
    def add_tail(self, item: T) -> None:

        self.__queue.append(item)

    # предусловие: очередь не пустая
    # постусловие: из начала очереди удалён элемент
    def remove_front(self) -> None:

        if self.size() > 0:
            self.__queue.pop(0)
            self.__remove_front_status = self.REMOVE_FRONT_OK
        else:
            self.__remove_front_status = self.REMOVE_FRONT_ERR


class Queue(ParentQueue):
    ...


class TwoWayQueue(ParentQueue):

    GET_TAIL_OK = 0
    GET_TAIL_ERR = 1

    REMOVE_TAIL_OK = 0
    REMOVE_TAIL_ERR = 1

    __get_tail_status: int
    __remove_tail_status: int

    # запросы
    # предусловие: очередь не пустая
    def get_tail(self) -> T:

        if self.size() > 0:
            result = self.__queue[-1]
            self.__get_tail_status = self.GET_TAIL_OK
        else:
            result = 0
            self.__get_tail_status = self.GET_TAIL_ERR
        return result

    def get_get_tail_status(self) -> int:

        return self.__get_tail_status

    def get_remove_tail_status(self) -> int:

        return self.__remove_tail_status

    # команды
    # постусловие: в начало очереди добавлен элемент
    def add_front(self, item: T) -> None:

        self.__queue.insert(0, item)

    # предусловие: очередь не пустая
    # постусловие: из конца очереди удалён элемент
    def remove_tail(self) -> None:

        if self.size() > 0:
            self.__queue.pop(-1)
            self.__remove_tail_status = self.REMOVE_TAIL_OK
        else:
            self.__remove_tail_status = self.REMOVE_TAIL_ERR
