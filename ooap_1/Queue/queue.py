# АТД ParentQueue
#
# abstract class ParentQueue<T>
#
#   public void push_back(<T> value) // добавление в конец очереди
#       - постусловие: в конец очереди добавлен новый элемент
#
#   public void pop_front() // удаление первого элемента в очереди
#       - предусловие: очередь не пуста
#       - постусловие: из очереди удален первый элемент
#
#   public void clear() // очистка очереди
#
#   public <T> get_front() // получение первого элемента
#       - предусловие: очередь не пуста
#       - постусловие: взят первый элемент из очереди
#
#   public int size() // получение размера
#       - постусловие: получен размер очереди
#
#   public int get_push_back_status() // статус добавления в конец очереди
#   public int get_get_front_status() // статус получения первого элемента из очереди
#   public int get_pop_front_status() // статус удаления первого элемента из очереди

# АТД Queue
# abstract class Queue<T> extends ParentQueue

# АТД Deque
# abstract class Deque<T> extends ParentQueue
#
#   public void push_front(<T> value) // добавление в начало очереди
#       - постусловие: в начало очереди добавлен новый элемент
#
#   public void pop_back() // удаление последнего элемента в очереди
#       - предусловие: очередь не пуста
#       - постусловие: из очереди удален последний элемент
#
#   public <T> get_back() // получение последнего элемента
#       - предусловие: очередь не пуста
#       - постусловие: взят последний элемент из очереди
#
#   public int get_push_front_status() // статус добавления в начало очереди
#   public int get_get_back_status() // статус получения последнего элемента из очереди
#   public int get_pop_back_status() // статус удаления последнего элемента из очереди


class ParentQueue:
    STATUS_NIL = 0
    STATUS_OK = 1
    STATUS_ERR = 2

    def __init__(self):
        self.queue = []

        self.push_back_status = self.STATUS_NIL
        self.get_front_status = self.STATUS_NIL
        self.pop_front_status = self.STATUS_NIL

    def push_back(self, value):
        self.queue.append(value)
        self.push_back_status = self.STATUS_OK

    def pop_front(self):
        if self.size() == 0:
            self.pop_front_status = self.STATUS_ERR
        else:
            del self.queue[0]
            self.pop_front_status = self.STATUS_OK

    def get_front(self):
        if self.size() == 0:
            result = 0
            self.get_front_status = self.STATUS_ERR
        else:
            result = self.queue[0]
            self.get_front_status = self.STATUS_OK

        return result

    def clear(self):
        self.queue = []

        self.push_back_status = self.STATUS_NIL
        self.get_front_status = self.STATUS_NIL
        self.pop_front_status = self.STATUS_NIL

    def size(self):
        return len(self.queue)

    def get_push_back_status(self):
        return self.push_back_status

    def get_get_front_status(self):
        return self.get_front_status

    def get_pop_front_status(self):
        return self.pop_front_status


class Queue(ParentQueue):
    pass


class Deque(ParentQueue):
    def __init__(self):
        super().__init__()

        self.push_front_status = self.STATUS_NIL
        self.pop_back_status = self.STATUS_NIL
        self.get_back_status = self.STATUS_NIL

    def push_front(self, value):
        self.queue.insert(0, value)
        self.push_front_status = self.STATUS_OK

    def pop_back(self):
        if self.size() == 0:
            self.pop_back_status = self.STATUS_ERR
        else:
            self.queue.pop()
            self.pop_back_status = self.STATUS_OK

    def get_back(self):
        if self.size() == 0:
            result = 0
            self.get_back_status = self.STATUS_ERR
        else:
            result = self.queue[-1]
            self.get_back_status = self.STATUS_OK

        return result

    def get_push_front_status(self):
        return self.push_front_status

    def get_pop_back_status(self):
        return self.pop_back_status

    def get_get_back_status(self):
        return self.get_back_status
