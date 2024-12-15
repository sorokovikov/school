from typing import Generic, TypeVar

T = TypeVar("T")


class BoundedStack(Generic[T]):

    POP_NIL = 0
    POP_OK = 1
    POP_ERR = 2

    PEAK_NIL = 0
    PEAK_OK = 1
    PEAK_ERR = 2

    PUSH_NIL = 0
    PUSH_OK = 1
    PUSH_ERR = 2

    __max_size: int
    __stack: list[T]
    __pop_status: int
    __peak_status: int
    __push_status: int

    def __init__(self, max_size: int = 32):

        self.__max_size = max_size
        self.clear()

    # предусловие: размер стека меньше чем его максимально допустимый размер
    # постусловие: в стек добавлено новое значение
    def push(self, value: T) -> None:

        if self.size() < self.__max_size:
            self.__stack.append(value)
            self.__push_status = self.PUSH_OK
        else:
            self.__push_status = self.PUSH_ERR

    # предусловие: стек не пустой;
    # постусловие: из стека удалён верхний элемент
    def pop(self) -> None:

        if self.size() > 0:
            self.__stack.pop(-1)
            self.__pop_status = self.POP_OK
        else:
            self.__pop_status = self.POP_ERR

    # предусловие: стек не пустой
    def peak(self) -> T:

        if self.size() > 0:
            result = self.__stack[-1]
            self.__peak_status = self.PEAK_OK
        else:
            result = 0
            self.__peak_status = self.PEAK_ERR
        return result

    def size(self) -> int:

        return len(self.__stack)

    # постусловие: из стека удалятся все значения
    def clear(self) -> None:

        self.__stack: list[T] = []

        self.__pop_status = self.POP_NIL
        self.__peak_status = self.PEAK_NIL
        self.__push_status = self.PUSH_NIL

    def get_pop_status(self) -> int:

        return self.__pop_status

    def get_peak_status(self) -> int:

        return self.__peak_status

    def get_push_status(self) -> int:

        return self.__push_status
