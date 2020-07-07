class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        """
        в качестве value поступают строки!
        всегда возвращает корректный индекс слота
        """
        str_sum = 0
        for i in range(len(value)):
            str_sum += ord(value[i]) * i + 1

        return str_sum % (len(self.slots) - 1)

    def seek_slot(self, value):
        """
        находит индекс пустого слота для значения, или None
        """
        index = self.hash_fun(value)

        if self.slots[index] is not None:
            i = index + self.step
            iters = 0
            while iters <= len(self.slots) // (len(self.slots) // self.step):
                if i >= len(self.slots):
                    i = i - len(self.slots)

                if self.slots[i] is None:
                    return i

                i += self.step
                iters += 1

            return None
        else:
            return index

    def put(self, value):
        """
        записываем значение по хэш-функции и
        возвращает индекс слота или None,
        если из-за коллизий элемент не удаётся разместить
        """
        index = self.seek_slot(value)

        if index is None:
            return None

        self.slots[index] = value
        return index

    def find(self, value):
        """
        находит индекс слота со значением, или None
        """
        index = self.hash_fun(value)

        if self.slots[index] != value:
            i = index + self.step
            iters = 0
            while iters <= len(self.slots) // (len(self.slots) // self.step):
                if i >= len(self.slots):
                    i = i - len(self.slots)

                if self.slots[i] == value:
                    return i

                i += self.step
                iters += 1

            return None

        return index
