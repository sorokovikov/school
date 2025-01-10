from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):

    FRONT_OK = 0
    FRONT_ERR = 1

    REMOVE_FRONT_OK = 0
    REMOVE_FRONT_ERR = 1

    __front_status: int
    __remove_front_status: int

    # конструктор
    # постусловие: создан новый объект пустой очереди
    def __init__(self):

        self.__queue: list[T] = []

    # запросы
    def size(self) -> int:

        return len(self.__queue)

    def get_front_status(self) -> int:

        return self.__front_status

    def get_remove_front_status(self) -> int:

        return self.__remove_front_status

    # предусловие: очередь непустая
    def front(self) -> T:

        if self.size() > 0:
            result = self.__queue[0]
            self.__front_status = self.FRONT_OK
        else:
            result = 0
            self.__front_status = self.FRONT_ERR
        return result

    # команды
    # постусловие: в конец очереди добавлен элемент
    def enqueue(self, item: T) -> None:

        self.__queue.append(item)

    # предусловие: очередь не пустая
    # постусловие: из начала очереди удалён элемент
    def remove_front(self) -> None:

        if self.size() > 0:
            self.__queue.pop(0)
            self.__remove_front_status = self.REMOVE_FRONT_OK
        else:
            self.__remove_front_status = self.REMOVE_FRONT_ERR
