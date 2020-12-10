# АТД Queue
#
# abstract class Queue<T>
#
#   public void put(<T> value) // добавление в очередь
#       - постусловие: в очередь добавлен новый элемент
#
#   public void remove() // удаление первого элемента в очереди
#       - предусловие: очередь не пуста
#       - постусловие: из очереди удален первый элемент
#
#   public void clear() // очистка очереди
#
#   public <T> get() // получение первого элемента
#       - предусловие: очередь не пуста
#       - постусловие: взят первый элемент из очереди
#
#   public int size() // получение размера
#       - постусловие: получен размер очереди
#
#   public int get_put_status() // статус добавления в очередь
#   public int get_get_status() // статус получения элемента из очереди
#   public int get_remove_status() // статус удаления первого элемента из очереди


class Queue:
    STATUS_NIL = 0
    STATUS_OK = 1
    STATUS_ERR = 2

    def __init__(self):
        self.queue = []

        self.put_status = self.STATUS_NIL
        self.get_status = self.STATUS_NIL
        self.remove_status = self.STATUS_NIL

    def put(self, value):
        self.queue.append(value)
        self.put_status = self.STATUS_OK

    def remove(self):
        if self.size() == 0:
            self.remove_status = self.STATUS_ERR
        else:
            del self.queue[0]
            self.remove_status = self.STATUS_OK

    def get(self):
        if self.size() == 0:
            result = 0
            self.get_status = self.STATUS_ERR
        else:
            result = self.queue[0]
            self.get_status = self.STATUS_OK

        return result

    def clear(self):
        self.queue = []

        self.put_status = self.STATUS_NIL
        self.get_status = self.STATUS_NIL
        self.remove_status = self.STATUS_NIL

    def size(self):
        return len(self.queue)

    def get_put_status(self):
        return self.put_status

    def get_get_status(self):
        return self.get_status

    def get_remove_status(self):
        return self.remove_status
