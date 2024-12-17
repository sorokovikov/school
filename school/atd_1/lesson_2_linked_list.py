from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Node(Generic[T]):

    def __init__(self, value: T):
        self.value = value
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class LinkedList(Generic[T]):

    GET_NIL = 0
    GET_OK = 1
    GET_ERR = 2

    IS_HEAD_NIL = 0
    IS_HEAD_OK = 1
    IS_HEAD_ERR = 2

    IS_TAIL_NIL = 0
    IS_TAIL_OK = 1
    IS_TAIL_ERR = 2

    HEAD_NIL = 0
    HEAD_OK = 1
    HEAD_ERR = 2

    TAIL_NIL = 0
    TAIL_OK = 1
    TAIL_ERR = 2

    RIGHT_NIL = 0
    RIGHT_OK = 1
    RIGHT_ERR = 2

    PUT_RIGHT_NIL = 0
    PUT_RIGHT_OK = 1
    PUT_RIGHT_ERR = 2

    PUT_LEFT_NIL = 0
    PUT_LEFT_OK = 1
    PUT_LEFT_ERR = 2

    REMOVE_NIL = 0
    REMOVE_OK = 1
    REMOVE_ERR = 2

    ADD_TO_EMPTY_OK = 1
    ADD_TO_EMPTY_ERR = 2

    ADD_TAIL_NIL = 0
    ADD_TAIL_OK = 1
    ADD_TAIL_ERR = 2

    REPLACE_NIL = 0
    REPLACE_OK = 1
    REPLACE_ERR = 2

    FIND_NIL = 0
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
            self.__get_status = LinkedList.GET_OK
        else:
            result = 0
            self.__get_status = LinkedList.GET_ERR
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
            self.__is_head_status = LinkedList.IS_HEAD_OK
        else:
            result = False
            self.__is_head_status = LinkedList.IS_HEAD_ERR

        return result

    # предусловие: список не пустой
    def is_tail(self) -> bool:
        """находится ли курсор в конце списка?"""

        if self.is_value():
            result = self.__cursor is self.__tail
            self.__is_tail_status = LinkedList.IS_TAIL_OK
        else:
            result = False
            self.__is_tail_status = LinkedList.IS_TAIL_ERR

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
            self.__head_status = LinkedList.HEAD_OK
        else:
            self.__head_status = LinkedList.HEAD_ERR

    # предусловие: список не пустой
    # постусловие: курсор перемещается на последний узел
    def tail(self) -> None:
        """установить курсор на последний узел в списке"""

        if self.is_value():
            self.__cursor = self.__tail
            self.__tail_status = LinkedList.TAIL_OK
        else:
            self.__tail_status = LinkedList.TAIL_ERR

    # предусловие: список не пустой
    # предусловие: справа от узла, на котором находится курсор, есть узел
    # постусловие: курсор перемещается на узел справа
    def right(self) -> None:
        """сдвинуть курсор на один узел вправо"""

        if self.is_value() and self.__cursor.next is not None:
            self.__cursor = self.__cursor.next
            self.__right_status = LinkedList.RIGHT_OK
        else:
            self.__right_status = LinkedList.RIGHT_ERR

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

            self.__put_right_status = LinkedList.PUT_RIGHT_OK
        else:
            self.__put_right_status = LinkedList.PUT_RIGHT_ERR

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

            self.__put_left_status = LinkedList.PUT_LEFT_OK
        else:
            self.__put_left_status = LinkedList.PUT_LEFT_ERR

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

            self.__remove_status = LinkedList.REMOVE_OK
        else:
            self.__remove_status = LinkedList.REMOVE_ERR

    # постусловие: из списка удаляются все узлы
    def clear(self) -> None:
        """очистить список"""

        self.__head: Optional[Node[T]] = None
        self.__tail: Optional[Node[T]] = None
        self.__cursor: Optional[Node[T]] = None

        self.__get_status = LinkedList.GET_NIL
        self.__is_head_status = LinkedList.IS_HEAD_NIL
        self.__is_tail_status = LinkedList.IS_TAIL_NIL
        self.__head_status = LinkedList.HEAD_NIL
        self.__tail_status = LinkedList.TAIL_NIL
        self.__right_status = LinkedList.RIGHT_NIL
        self.__put_right_status = LinkedList.PUT_RIGHT_NIL
        self.__put_left_status = LinkedList.PUT_LEFT_NIL
        self.__remove_status = LinkedList.REMOVE_NIL
        self.__add_tail_status = LinkedList.ADD_TAIL_NIL
        self.__replace_status = LinkedList.REPLACE_NIL
        self.__find_status = LinkedList.FIND_NIL

    # предусловие: список пуст
    # постусловие: в пустой список добавляется узел
    def add_to_empty(self, value: T) -> None:
        """добавить новый узел в пустой список"""

        if not self.is_value():
            self.__head = Node(value)
            self.__tail = self.__head
            self.__cursor = self.__head

            self.__add_to_empty_status = LinkedList.ADD_TO_EMPTY_OK
        else:
            self.__add_to_empty_status = LinkedList.ADD_TO_EMPTY_ERR

    # предусловие: список не пустой
    # постусловие: в хвост списка добавляется новый узел
    def add_tail(self, value: T) -> None:
        """добавить новый узел в хвост списка"""

        if self.is_value():
            self.__tail.next = Node(value)
            self.__tail.next.prev = self.__tail
            self.__tail = self.__tail.next

            self.__add_tail_status = LinkedList.ADD_TAIL_OK
        else:
            self.__add_tail_status = LinkedList.ADD_TAIL_ERR

    # предусловие: список не пустой
    # постусловие: значение в узле, на котором установлен курсор, заменяется на переданное
    def replace(self, value: T) -> None:
        """заменить значение текущего узла на заданное"""

        if self.is_value():
            self.__cursor.value = value

            self.__replace_status = LinkedList.REPLACE_OK
        else:
            self.__replace_status = LinkedList.REPLACE_ERR

    # предусловие: искомое значение должно быть в части списка после указателя
    # постусловие: курсор устанавливается на первый узел с искомым значением
    def find(self, value: T) -> None:
        """установить курсор на следующий узел с искомым значением (по отношению к текущему узлу)"""

        if found := self.__find(self.__cursor.next, value):
            self.__cursor = found

            self.__find_status = LinkedList.FIND_OK
        else:
            self.__find_status = LinkedList.FIND_ERR

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
