# АТД ParentList

# abstract class ParentList<T>
#     public void ParentList<T> // конструктор
#
#     private <T> head // голова
#     private <T> tail // хвост
#     private <T> cursor // курсор
#
#     // команды
#     public void head() // установить курсор на первый узел в списке
#         - предусловие: список не пустой
#         - постусловие: курсор установлен на первый узел
#
#     public void tail() // установить курсор на последний узел в списке
#         - предусловие: список не пустой
#         - постусловие: курсор установлен на последний узел
#
#     public void right() // сдвинуть курсор на один узел вправо
#         - предусловие: список не пустой, есть элемент справа от курсора
#         - постусловие: курсор сдвинут вправо
#
#     public void put_right(<Node> value) // вставить следом за текущим узлом новый узел с заданным значением
#         - предусловие: список не пустой
#         - постусловие: справа от курсора добавлен новый элемент
#
#     public void put_left(<Node> value) // вставить перед текущим узлом новый узел с заданным значением
#         - предусловие: список не пустой
#         - постусловие: слева от курсора добавлен новый элемент
#
#     public void remove() // удалить текущий узел (курсор смещается к правому соседу, если он есть, в противном случае курсор смещается к левому соседу, если он есть)
#         - предусловие: список не пустой
#         - текущий узел удалён, курсор смещён к правому соседу, если он есть, в противном случае курсор смещён к левому соседу, если он есть
#
#     public void clear() // очистить список
#         - постусловие: список очищен
#
#     public void add_tail(<Node> value) // добавить новый узел в хвост списка
#         - постусловие: элемент добавлен в хвост
#
#     public void replace(<Node> value) // заменить значение текущего узла на заданное
#         - предусловие: список не пустой
#         - постусловие: значение текущего узла заменено на новое
#
#     public void find(<T> value) // установить курсор на следующий узел с искомым значением (по отношению к текущему узлу)
#         - постусловие: курсор установлен на искомом
#
#     public void remove_all(<T> value) // удалить в списке все узлы с заданным значением
#         - постусловие: удалены всё с заданым значением
#
#     // запросы
#     public <T> get() // получить значение текущего узла
#         - предусловие: список не пустой
#
#     public <int> size() // посчитать количество узлов в списке
#     public <bool> is_head() // находится ли курсор в начале списка?
#     public <bool> is_tail() // находится ли курсор в конце списка?
#     public <bool> is_value() // установлен ли курсор на какой-либо узел в списке (по сути, непустой ли список).
#
#     // запросы статусов (возможные значения статусов)
#     public int get_head_status(); // успешно; список пуст
#     public int get_tail_status(); // успешно; список пуст
#     public int get_right_status(); // успешно; правее нету элемента
#     public int get_put_right_status(); // успешно; список пуст
#     public int get_put_left_status(); // успешно; список пуст
#     public int get_remove_status(); // успешно; список пуст
#     public int get_replace_status(); // успешно; список пуст
#     public int get_find_status(); // следующий найден; следующий не найден; список пуст
#     public int get_get_status(); // успешно; список пуст


# АТД LinkedList
# class LinkedList extends ParentList

# АТД TwoWayList extends ParentList
# class TwoWayList extends ParentList
#
#   // команды
#   public void left(): // сдвинуть курсор на один элемент влево
#       - предусловие: список не пустой, есть элемент справа от курсора
#       - постусловие: курсор сдвинут влево
#
#   // запросы
#   public int get_left_status(): // успешно; левее нету элемента
from abc import ABC


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None


class ParentList(ABC):
    STATUS_NIL = 0
    STATUS_OK = 1
    STATUS_ERR = 2

    def __init__(self):
        self.list_head = None
        self.list_tail = None
        self.cursor = None

        self.list_head_status = self.STATUS_NIL
        self.list_tail_status = self.STATUS_NIL
        self.right_status = self.STATUS_NIL
        self.put_right_status = self.STATUS_NIL
        self.put_left_status = self.STATUS_NIL
        self.remove_status = self.STATUS_NIL
        self.add_list_tail_status = self.STATUS_NIL
        self.replace_status = self.STATUS_NIL
        self.get_status = self.STATUS_NIL

    def head(self):
        if self.list_head is None:
            self.list_head_status = self.STATUS_ERR
        else:
            self.cursor = self.list_head
            self.list_head_status = self.STATUS_OK

    def tail(self):
        if self.list_tail is None:
            self.list_tail_status = self.STATUS_ERR
        else:
            self.cursor = self.list_tail
            self.list_tail_status = self.STATUS_OK

    def right(self):
        if self.list_head is None or self.cursor.next is None:
            self.right_status = self.STATUS_ERR
        else:
            self.cursor = self.cursor.next
            self.right_status = self.STATUS_OK

    def put_right(self, value: Node):
        if self.list_head is None:
            self.put_right_status = self.STATUS_ERR
        else:
            value.prev = self.cursor
            value.next = self.cursor.next

            self.cursor.next.prev = value
            self.cursor.next = value

            self.put_right_status = self.STATUS_OK

    def put_left(self, value: Node):
        if self.list_head is None:
            self.put_left_status = self.STATUS_ERR
        else:
            value.prev = self.cursor.prev
            value.next = self.cursor

            if self.cursor.prev is not None:
                self.cursor.prev.next = value

            self.cursor.prev = value
            self.put_left_status = self.STATUS_OK

    def remove(self):
        if self.list_head is None:
            self.remove_status = self.STATUS_ERR
        else:
            prev = self.cursor.prev
            next = self.cursor.next

            prev.next = next
            next.prev = prev

            if self.cursor.next is not None:
                self.cursor = self.cursor.next
            else:
                self.cursor = self.cursor.prev

            self.remove_status = self.STATUS_OK

    def clear(self):
        self.list_head = None
        self.list_tail = None
        self.cursor = None

    def add_tail(self, value: Node):
        if self.list_head is None:
            self.list_head = value
            self.list_tail = value
        else:
            self.list_tail.next = value
            value.prev = self.list_tail

            self.list_tail = value

        self.add_list_tail_status = self.STATUS_OK

    def replace(self, node: Node):
        if self.list_head is None:
            self.replace_status = self.STATUS_ERR
        else:
            self.cursor.value = node.value
            self.replace_status = self.STATUS_OK

    def find(self, value):
        node = self.cursor

        while node is not None:
            if node.value == value:
                self.cursor = node
                break

            node = node.next

    def get(self) -> 'Node':
        if self.head is None or self.cursor is None:
            self.get_status = self.STATUS_ERR
        else:
            self.get_status = self.STATUS_OK
            return self.cursor.value

    def size(self) -> int:
        count = 0
        node = self.list_head

        while node is not None:
            count += 1
            node = node.next

        return count

    def is_head(self) -> bool:
        return self.cursor == self.list_head

    def is_tail(self) -> bool:
        return self.cursor == self.list_tail

    def is_value(self) -> bool:
        return self.cursor is not None

    def get_list_head_status(self):
        return self.list_head_status

    def get_list_tail_status(self):
        return self.list_tail_status

    def get_right_status(self):
        return self.right_status

    def get_put_right_status(self):
        return self.put_right_status

    def get_put_left_status(self):
        return self.put_left_status

    def get_remove_status(self):
        return self.remove_status

    def get_add_tail_status(self):
        return self.add_list_tail_status

    def get_replace_status(self):
        return self.replace_status

    def get_get_status(self):
        return self.get_status


class LinkedList(ParentList):
    pass


class TwoWayList(ParentList):
    def __init__(self):
        ParentList.__init__(self)
        self.left_status = self.STATUS_NIL

    def left(self):
        if self.list_head is None or self.cursor.prev is None:
            self.left_status = self.STATUS_ERR
        else:
            self.cursor = self.cursor.prev
            self.left_status = self.STATUS_OK

    def get_left_status(self):
        return self.left_status
