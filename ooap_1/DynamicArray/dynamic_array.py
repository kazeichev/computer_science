# АТД DynamicArray
#
# abstract class DynamicArray<T>
#
#   private int realSize
#   private int bufferSize
#   private <T> buffer
#
#   public void DynamicArray<T> // конструктор
#       - постусловие: создан пустой массив
#
#   // команды
#   private void grow()
#   public void add(int i, <T> value) // добавление элемента согласно индексу
#       - предусловие: i в пределах размера массива
#       - постусловие: в позицию i добавлено значение value
#
#   public void remove(int i) // удаление элемента согласно индексу
#       - предусловие: массив не пустой, i в пределах размера массива
#       - постусловие: удален элемент с индексом i
#
#   // запросы
#   public <T> get(int i) // получение элемента по индексу
#       - предусловие: i в пределах размера массива
#
#   public int size() // получение размера массива
#
#   public int get_add_status()
#   public int get_remove_status()
