from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Node(Generic[T]):

    def __init__(self, value: T):
        self.value = value
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class ParentList(Generic[T]):

    GET_OK = 1
    GET_ERR = 2

    IS_HEAD_OK = 1
    IS_HEAD_ERR = 2

    IS_TAIL_OK = 1
    IS_TAIL_ERR = 2

    HEAD_OK = 1
    HEAD_ERR = 2

    TAIL_OK = 1
    TAIL_ERR = 2

    RIGHT_OK = 1
    RIGHT_ERR = 2

    PUT_RIGHT_OK = 1
    PUT_RIGHT_ERR = 2

    PUT_LEFT_OK = 1
    PUT_LEFT_ERR = 2

    REMOVE_OK = 1
    REMOVE_ERR = 2

    ADD_TO_EMPTY_OK = 1
    ADD_TO_EMPTY_ERR = 2

    ADD_TAIL_OK = 1
    ADD_TAIL_ERR = 2

    REPLACE_OK = 1
    REPLACE_ERR = 2

    FIND_OK = 1
    FIND_ERR = 2

    __head: Optional[Node[T]]
    __tail: Optional[Node[T]]
    __cursor: Optional[Node[T]]

    __get_status: int
    __is_head_status: int
    __is_tail_status: int
    __head_status: int
    __tail_status: int
    __right_status: int
    __put_right_status: int
    __put_left_status: int
    __remove_status: int
    __add_to_empty_status: int
    __add_tail_status: int
    __replace_status: int
    __find_status: int

    # конструктор
    # постусловие: создан новый пустой связный список
    def __init__(self):

        self.clear()

    # запросы:
    # предусловие: список не пустой
    def get(self) -> T:
        """получить значение текущего узла"""

        if self.is_value():
            result = self.__cursor.value
            self.__get_status = ParentList.GET_OK
        else:
            result = 0
            self.__get_status = ParentList.GET_ERR
        return result


    def size(self) -> int:
        """посчитать количество узлов в списке"""

        return self.__size(self.__head, 0)

    def __size(self, node: Optional[Node[T]], count: int) -> int:

        if node is None:
            return count
        return self.__size(node.next, count + 1)

    # предусловие: список не пустой
    def is_head(self) -> bool:
        """находится ли курсор в начале списка?"""

        if self.is_value():
            result = self.__cursor is self.__head
            self.__is_head_status = ParentList.IS_HEAD_OK
        else:
            result = False
            self.__is_head_status = ParentList.IS_HEAD_ERR

        return result

    # предусловие: список не пустой
    def is_tail(self) -> bool:
        """находится ли курсор в конце списка?"""

        if self.is_value():
            result = self.__cursor is self.__tail
            self.__is_tail_status = ParentList.IS_TAIL_OK
        else:
            result = False
            self.__is_tail_status = ParentList.IS_TAIL_ERR

        return result

    def is_value(self) -> bool:
        """установлен ли курсор на какой-либо узел в списке (по сути, непустой ли список)"""

        return self.__cursor is not None

    # команды:
    # предусловие: список не пустой
    # постусловие: курсор перемещается на первый узел
    def head(self) -> None:
        """установить курсор на первый узел в списке"""

        if self.is_value():
            self.__cursor = self.__head
            self.__head_status = ParentList.HEAD_OK
        else:
            self.__head_status = ParentList.HEAD_ERR

    # предусловие: список не пустой
    # постусловие: курсор перемещается на последний узел
    def tail(self) -> None:
        """установить курсор на последний узел в списке"""

        if self.is_value():
            self.__cursor = self.__tail
            self.__tail_status = ParentList.TAIL_OK
        else:
            self.__tail_status = ParentList.TAIL_ERR

    # предусловие: список не пустой
    # предусловие: справа от узла, на котором находится курсор, есть узел
    # постусловие: курсор перемещается на узел справа
    def right(self) -> None:
        """сдвинуть курсор на один узел вправо"""

        if self.is_value() and self.__cursor.next is not None:
            self.__cursor = self.__cursor.next
            self.__right_status = ParentList.RIGHT_OK
        else:
            self.__right_status = ParentList.RIGHT_ERR

    # предусловие: список не пустой
    # постусловие: справа от узла, на котором находится курсор, вставляется новый узел
    def put_right(self, value: T) -> None:
        """вставить следом за текущим узлом новый узел с заданным значением"""

        if self.is_value():
            new_node = Node(value)
            new_node.next = self.__cursor.next
            if self.__cursor.next is not None:
                self.__cursor.next.prev = new_node
            self.__cursor.next = new_node
            self.__cursor.next.prev = self.__cursor

            if self.__cursor.next.next is None:
                self.__tail = self.__cursor.next

            self.__put_right_status = ParentList.PUT_RIGHT_OK
        else:
            self.__put_right_status = ParentList.PUT_RIGHT_ERR

    # предусловие: список не пустой
    # постусловие: слева от узла, на котором находится курсор, вставляется новй узел
    def put_left(self, value: T) -> None:
        """вставить перед текущим узлом новый узел с заданным значением"""

        if self.is_value():
            new_node = Node(value)
            new_node.prev = self.__cursor.prev
            if self.__cursor.prev is not None:
                self.__cursor.prev.next = new_node
            self.__cursor.prev = new_node
            self.__cursor.prev.next = self.__cursor

            if self.__cursor.prev.prev is None:
                self.__head = self.__cursor.prev

            self.__put_left_status = ParentList.PUT_LEFT_OK
        else:
            self.__put_left_status = ParentList.PUT_LEFT_ERR

    # предусловие: список не пустой
    # постусловие: узел, на котором находится курсор, удаляется
    # постусловие: курсор перемещается на узел справа от удаляемого, если он есть
    # постусловие: если узла справа от курсора нет, то курсор перемещается на узел слева от удаляемого
    # постусловие: если узла слева от курсора нет, то список пуст
    def remove(self) -> None:
        """
        удалить текущий узел (курсор смещается к правому соседу, если он есть,
        в противном случае курсор смещается к левому соседу, если он есть)
        """

        if self.is_value():
            if self.__cursor.next is not None and self.__cursor.prev is not None:
                self.__cursor.prev.next = self.__cursor.next
                self.__cursor.next.prev = self.__cursor.prev
                self.__cursor = self.__cursor.next

            if self.__cursor.next is None and self.__cursor.prev is not None:
                self.__cursor.prev.next = None
                self.__tail = self.__cursor.prev
                self.__cursor = self.__cursor.prev

            if self.__cursor.next is None and self.__cursor.prev is None:
                self.clear()

            self.__remove_status = ParentList.REMOVE_OK
        else:
            self.__remove_status = ParentList.REMOVE_ERR

    # постусловие: из списка удаляются все узлы
    def clear(self) -> None:
        """очистить список"""

        self.__head: Optional[Node[T]] = None
        self.__tail: Optional[Node[T]] = None
        self.__cursor: Optional[Node[T]] = None

    # предусловие: список пуст
    # постусловие: в пустой список добавляется узел
    def add_to_empty(self, value: T) -> None:
        """добавить новый узел в пустой список"""

        if not self.is_value():
            self.__head = Node(value)
            self.__tail = self.__head
            self.__cursor = self.__head

            self.__add_to_empty_status = ParentList.ADD_TO_EMPTY_OK
        else:
            self.__add_to_empty_status = ParentList.ADD_TO_EMPTY_ERR

    # предусловие: список не пустой
    # постусловие: в хвост списка добавляется новый узел
    def add_tail(self, value: T) -> None:
        """добавить новый узел в хвост списка"""

        if self.is_value():
            self.__tail.next = Node(value)
            self.__tail.next.prev = self.__tail
            self.__tail = self.__tail.next

            self.__add_tail_status = ParentList.ADD_TAIL_OK
        else:
            self.__add_tail_status = ParentList.ADD_TAIL_ERR

    # предусловие: список не пустой
    # постусловие: значение в узле, на котором установлен курсор, заменяется на переданное
    def replace(self, value: T) -> None:
        """заменить значение текущего узла на заданное"""

        if self.is_value():
            self.__cursor.value = value

            self.__replace_status = ParentList.REPLACE_OK
        else:
            self.__replace_status = ParentList.REPLACE_ERR

    # предусловие: искомое значение должно быть в части списка после указателя
    # постусловие: курсор устанавливается на первый узел с искомым значением
    def find(self, value: T) -> None:
        """установить курсор на следующий узел с искомым значением (по отношению к текущему узлу)"""

        if found := self.__find(self.__cursor.next, value):
            self.__cursor = found

            self.__find_status = ParentList.FIND_OK
        else:
            self.__find_status = ParentList.FIND_ERR

    # постусловие: из списка удаляются все узлы с заданным значением
    def remove_all(self, value: T) -> None:
        """удалить в списке все узлы с заданным значением"""

        self.__remove_all(self.__head, value)

    def __find(self, node: Optional[Node[T]], value: T) -> Optional[Node[T]]:

        if node is None:
            return None
        if node.value == value:
            return node
        return self.__find(node.next, value)

    def __remove_all(self, node: Optional[Node[T]], value: T) -> None:

        if node is None:
            return
        if node.value == value:
            if node.next is not None:
                node.next.prev = node.prev
            if node.next is not None and node.prev is None:
                self.__head = node.next

            if node.prev is not None:
                node.prev.next = node.next
            if node.prev is not None and node.next is None:
                self.__tail = node.prev

            if node is self.__cursor and node.next is not None:
                self.__cursor = node.next
            if node is self.__cursor and node.next is None and node.prev is not None:
                self.__cursor = node.prev

            if node.prev is None and node.next is None:
                self.clear()

        self.__remove_all(node.next, value)

    # дополнительные запросы статусов операций:
    def get_get_status(self) -> int:

        return self.__get_status

    def get_is_head_status(self) -> int:

        return self.__is_head_status

    def get_is_tail_status(self) -> int:

        return self.__is_tail_status

    def get_head_status(self) -> int:

        return self.__head_status

    def get_tail_status(self) -> int:

        return self.__tail_status

    def get_right_status(self) -> int:

        return self.__right_status

    def get_put_right_status(self) -> int:

        return self.__put_right_status

    def get_put_left_status(self) -> int:

        return self.__put_left_status

    def get_remove_status(self) -> int:

        return self.__remove_status

    def get_add_to_empty_status(self) -> int:

        return self.__add_to_empty_status

    def get_add_tail_status(self) -> int:

        return self.__add_tail_status

    def get_replace_status(self) -> int:

        return self.__replace_status

    def get_find_status(self) -> int:

        return self.__find_status


class LinkedList(ParentList):
    ...


class TwoWayList(ParentList):

    __left_status: int

    LEFT_OK = 1
    LEFT_ERR = 2

    # предусловие: слева от узла, на котором находится курсор, есть узел
    # постусловие: курсор перемещается на узел слева
    def left(self) -> None:

        if self.is_value() and self.__cursor.prev is not None:
            self.__cursor = self.__cursor.prev
            self.__left_status = TwoWayList.LEFT_OK
        else:
            self.__left_status = TwoWayList.LEFT_ERR

    def get_left_status(self) -> int:

        return self.__left_status
