# АТД HashTable
#
# abstract class HashTable<T>
#
#   public void HashTable(int maxSize) - конструктор с параметром максимального размера таблицы
#
#   // Команды
#   public void put(value) - добавление элемента
#       - предусловие: в таблице есть место
#       - постусловие: в таблицу добавлен новый элемент
#
#   public void pop(value) - удаление элемента
#       - предусловие: таблица не пуста
#       - постусловие: из таблицы удален элемент
#
#   // Запросы
#   public bool is_exist(value) - имеется ли элемент в таблице
#
#   public int size() - размер таблицы
#
#   public int get_put_status() - получение статуса команды put()
#   public int get_pop_status() - получение статуса команды pop()


class HashTable:
    STATUS_NIL = 0
    STATUS_OK = 1
    STATUS_ERR = 2

    def __init__(self, max_size):
        self.maxSize = max_size
        self.slots = [None] * max_size

        self.put_status = self.STATUS_NIL
        self.pop_status = self.STATUS_NIL

    def hash_fun_1(self, value):
        return value % self.maxSize

    def hash_fun_2(self, value):
        random_number = self.maxSize // 2
        return random_number - (value % random_number)

    def seek_slot(self, value):
        """
        Поиск слота для вставки
        :param value:
        :return:
        """
        index_1 = self.hash_fun_1(value)

        if self.slots[index_1] is not None:
            index_2 = self.hash_fun_2(value)
            i = 0
            while i < self.maxSize:
                newIndex = (index_1 + i * index_2) % self.maxSize
                if self.slots[newIndex] is None:
                    return newIndex
                else:
                    i += 1

            return None
        else:
            return index_1

    def find_slot(self, value):
        """
        Поиск слота со значением
        :param value:
        :return:
        """
        index_1 = self.hash_fun_1(value)

        if self.slots[index_1] != value:
            index_2 = self.hash_fun_2(value)
            i = 0
            while i < self.maxSize:
                newIndex = (index_1 + i * index_2) % self.maxSize
                if self.slots[newIndex] == value:
                    return newIndex
                else:
                    i += 1

            return None
        else:
            return index_1

    def put(self, value):
        index = self.seek_slot(value)

        if index is None:
            self.put_status = self.STATUS_ERR
        else:
            self.slots[index] = value
            self.put_status = self.STATUS_OK

    def pop(self, value):
        index = self.find_slot(value)

        if index is None:
            self.pop_status = self.STATUS_ERR
        else:
            self.slots[index] = None
            self.pop_status = self.STATUS_OK

    def is_exist(self, value):
        index = self.find_slot(value)

        if index is None:
            result = False
        else:
            result = True

        return result

    def size(self):
        return len(self.slots)

    def get_put_status(self):
        return self.put_status

    def get_pop_status(self):
        return self.pop_status
