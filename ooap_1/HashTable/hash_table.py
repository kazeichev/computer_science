# АТД HashTable
#
# abstract class HashTable<T>
#
#   public void HashTable(int maxSize) - конструктор с параметром максимального размера таблицы
#
#   public void put(key, value) - добавление элемента по ключу
#       - постусловие: в таблицу добавлен новый элемент
#
#   // Команды
#   public void pop(key) - удаление элемента по ключу
#       - предусловие: таблица не пуста
#       - постусловие: из таблицы удален элемент
#
#   // Запросы
#   public <T> find(key) - получение элемента по ключу
#       - предусловие: список не пустой
#
#   public int get_put_status() - получение статуса команды put()
#   public int get_pop_status() - получение статуса команды pop()
#   public int get_find_status() - получение статуса команды find()

