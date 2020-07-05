class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.step = 3

    def __len__(self):
        return len(self.slots)

    def hash_fun(self, key):
        """
        в качестве key поступают строки!
        всегда возвращает корректный индекс слота
        """
        str_sum = 0
        for i in range(len(key)):
            str_sum += ord(key[i]) * i + 1

        return str_sum % (len(self.slots) - 1)

    def is_key(self, key):
        """
        возвращает True если ключ имеется,
        иначе False
        """
        index = self.hash_fun(key)
        if self.slots[index] != key:
            i = index + self.step
            iters = 0
            while iters <= len(self.slots) // (len(self.slots) // self.step):
                if i >= len(self.slots):
                    i = i - len(self.slots)

                if self.slots[i] == key:
                    return True

                i += self.step
                iters += 1

            return False
        return True

    def put(self, key, value):
        """
        гарантированно записываем
        значение value по ключу key
        """
        index = self.hash_fun(key)

        if self.slots[index] is None:
            self.slots[index] = key
            self.values[index] = value
        else:
            if self.slots[index] == key:
                self.values[index] = value
            else:
                i = index + self.step
                iters = 0
                while iters <= self.size:
                    if i >= len(self.slots):
                        i = i - len(self.slots)

                    if self.slots[i] is None:
                        self.slots[i] = key
                        self.values[i] = value

                    i += self.step
                    iters += 1

    def get(self, key):
        """
        возвращает value для key,
        или None если ключ не найден
        """
        index = self.hash_fun(key)

        if self.is_key(key) is False:
            return None

        if self.slots[index] != key:
            i = index + self.step
            iters = 0
            while iters <= self.size:
                if i >= len(self.slots):
                    i = i - len(self.slots)

                if self.slots[i] == key:
                    return self.values[i]

                i += self.step
                iters += 1

            return None
        return self.values[index]


class NativeCache(NativeDictionary):
    def __init__(self, sz):
        super().__init__(sz)
        self.hits = [0] * self.size

    def put(self, key, value):
        index = self.hash_fun(key)

        if self.slots[index] is None:
            self.slots[index] = key
            self.values[index] = value
            self.hits[index] = 0
        else:
            if self.slots[index] == key:
                self.values[index] = value
                self.hits[index] = 0
            else:
                i = index + self.step
                iters = 0
                while iters <= self.size:
                    if i >= len(self.slots):
                        i = i - len(self.slots)

                    if self.slots[i] is None:
                        self.slots[i] = key
                        self.values[i] = value
                        self.hits[i] = 0
                        return

                    i += self.step
                    iters += 1

            index = self.hits.index(min(self.hits))
            self.slots[index] = value
            self.values[index] = value
            self.hits[index] = 0

    def get(self, key):
        index = self.hash_fun(key)

        if self.is_key(key) is False:
            return None

        if self.slots[index] != key:
            i = index + self.step
            iters = 0
            while iters <= self.size:
                if i >= len(self.slots):
                    i = i - len(self.slots)

                if self.slots[i] == key:
                    self.hits[i] += 1
                    return self.values[i]

                i += self.step
                iters += 1

            return None

        self.hits[index] += 1
        return self.values[index]
