# АТД PowerSet
#
# abstract class PowerSet extends HashTable
#
#   public void PowerSet(int maxSize) - конструктор
#
#   public void put(value) - вставка элемента
#       - предусловие: в таблице есть место, во множестве нет такого же элемента
#       - постусловие: в таблицу добавлен новый элемент
#

from ooap_1.HashTable.hash_table import HashTable


class PowerSet(HashTable):
    def put(self, value):
        index = self.seek_slot(value)

        if self.is_exist(value) or index is None:
            self.put_status = self.STATUS_ERR
        else:
            self.slots[index] = value
            self.put_status = self.STATUS_OK
