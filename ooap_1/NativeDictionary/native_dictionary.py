# АТД NativeDictionary
#
# abstract class NativeDictionary<T>
#
#   public void NativeDictionary(int maxSize) - конструктор с параметром максимального размера
#
#   // команды
#   public void insert(string key, <T> value) - добавление нового значения по ключу
#       - предусловие: в словаре есть место
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
