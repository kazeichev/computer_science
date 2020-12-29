# АТД NativeDictionary
#
# abstract class NativeDictionary<T>
#
#   public void NativeDictionary() - конструктор
#
#   // команды
#   public void insert(string key, <T> value) - добавление нового значения по ключу
#       - постусловие: в словарь добавлен новый элемент по ключу, либо обновлен имеющийся
#
#   public void remove(string key) - удаление значения по ключу
#       - предусловие: ключ присутствует в словаре
#       - постусловие: из словаря удален элемент по ключу
#
#
#   // запросы
#   public <T> get(string key) - получет элемент по ключу
#       - предусловие: ключ присутствует в словаре
#
#   public bool is_exist(string key) - проверяет наличие ключа
#
#   public int size() - получает размер
#
#   public int get_insert_status() - получает статус команды вставки
#   public int get_remove_status() - получает статус команды удаления
#   public int get_get_status() - получает статус команды get

class NativeDictionary:
    STATUS_NIL = 0
    STATUS_OK = 1
    STATUS_ERR = 2

    def __init__(self):
        self.dictionary = {}

        self.insert_status = self.STATUS_NIL
        self.remove_status = self.STATUS_NIL
        self.get_status = self.STATUS_NIL

    def insert(self, key, value):
        self.dictionary[key] = value
        self.insert_status = self.STATUS_OK

    def remove(self, key):
        if self.is_exist(key):
            del self.dictionary[key]
            self.remove_status = self.STATUS_OK
        else:
            self.remove_status = self.STATUS_ERR

    def get(self, key):
        if self.is_exist(key):
            result = self.dictionary[key]
            self.get_status = self.STATUS_OK
        else:
            result = 0
            self.get_status = self.STATUS_ERR

        return result

    def is_exist(self, key):
        return key in self.dictionary

    def size(self):
        return len(self.dictionary)

    def get_insert_status(self):
        return self.insert_status

    def get_remove_status(self):
        return self.remove_status

    def get_get_status(self):
        return self.get_status
