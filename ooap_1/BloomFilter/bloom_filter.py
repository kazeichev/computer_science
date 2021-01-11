# АТД BloomFilter
#
# abstract class BloomFilter<T>
#
#   public void BloomFilter(int size) - конструктор, с параметром максимального размера
#
#   // команды
#   public void add(<T> value) - добавление значения в фильтр
#
#
#   // запросы
#   public bool is_value() - проверка наличия значения в фильтре
#       - постусловие: возвращает True при наличии значения в фильтре/False при отсутствии значения в фильтре
#
#
