# АТД BoundedStack
# class BoundedStack<T>
#   // Скрытые поля
#   private List stack // хранилище стека
#   private int peek_status // результат выполнения запроса peek()
#   private int pop_status // результат выполнения команды pop()
#
#   // интерфейс класса, реализующий АТД BoundedStack
#   public const int PUSH_NIL = 0;
#   public const int PUSH_OK = 1;
#   public const int PUSH_ERR = 2;
#   public const int POP_NIL = 0;
#   public const int POP_OK = 1;
#   public const int POP_ERR = 2;
#   public const int PEEK_NIL = 0;
#   public const int PEEK_OK = 1;
#   public const int PEEK_ERR = 2;
#
#   // команды
#   public void BoundedStack<T> // конструктор
#   public void push(T value) // команда добавления в стек
#   public void pop() // команда удаления элемента из стека
#   public void clear() // команда очистки стека
#
#   // запросы
#   public T peek() // запрос верхнего элемента стека
#   public int size() // запрос размера стека
#   public int get_push_status() // запрос статуса команды push()
#   public int get_pop_status() // запрос статуса команды pop()
#   public int get_peek_status() // запрос статуса запроса peek()

# Реализация АТД BoundedStack
class BoundedStack:
    # Константы
    STATUS_PUSH_NIL = 0
    STATUS_PUSH_OK = 1
    STATUS_PUSH_ERR = 2

    STATUS_POP_NIL = 0
    STATUS_POP_OK = 1
    STATUS_POP_ERR = 2

    STATUS_PEEK_NIL = 0
    STATUS_PEEK_OK = 1
    STATUS_PEEK_ERR = 2

    def __init__(self, max_size=32):
        # Хранилище
        self.stack = []

        # Статусы
        self.push_status = self.STATUS_PUSH_NIL
        self.pop_status = self.STATUS_POP_NIL
        self.peek_status = self.STATUS_PEEK_NIL

        # Размер
        self.max_size = max_size

    def push(self, value) -> None:
        if self.size() < self.max_size:
            self.stack.append(value)
            self.push_status = BoundedStack.STATUS_PUSH_OK
        else:
            self.push_status = BoundedStack.STATUS_PUSH_ERR

    def pop(self) -> None:
        if self.size() > 0:
            self.stack = self.stack[:-1]
            self.pop_status = BoundedStack.STATUS_POP_OK
        else:
            self.pop_status = BoundedStack.STATUS_POP_ERR

    def clear(self) -> None:
        self.stack = []

        self.push_status = BoundedStack.STATUS_PUSH_NIL
        self.pop_status = BoundedStack.STATUS_POP_NIL
        self.peek_status = BoundedStack.STATUS_PEEK_NIL

    def peek(self) -> int:
        if self.size() > 0:
            result = self.stack[-1]
            self.peek_status = BoundedStack.STATUS_PEEK_OK
        else:
            result = 0
            self.peek_status = BoundedStack.STATUS_PEEK_ERR

        return result

    def size(self) -> int:
        return len(self.stack)

    def get_push_status(self) -> int:
        return self.push_status

    def get_pop_status(self) -> int:
        return self.pop_status

    def get_peek_status(self) -> int:
        return self.peek_status

    def get_max_size(self) -> int:
        return self.max_size
