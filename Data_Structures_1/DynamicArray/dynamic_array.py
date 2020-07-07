import ctypes


class DynArray:
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i > len(self) or i < 0:
            raise IndexError("Incorrect index")

        if self.count >= self.capacity:
            self.resize(2 * self.capacity)

        is_next = False
        tmp_array = self.make_array(self.capacity)

        for j in range(len(self)):
            tmp_array[j] = self.array[j]

        for j in range(len(self) + 1):
            if j == i:
                self.array[j] = itm
                is_next = True
                continue

            if is_next:
                if (j - 1) >= 0:
                    self.array[j] = tmp_array[j - 1]
            else:
                self.array[j] = tmp_array[j]

        self.count += 1

    def delete(self, i):
        if len(self) == 0:
            raise IndexError("Incorrect index")

        if i > len(self) or i < 0:
            raise IndexError("Incorrect index")

        if len(self) < self.capacity // 2:
            new_capacity = int(self.capacity // 1.5)
            if new_capacity < 16:
                self.resize(16)
            else:
                self.resize(new_capacity)

        is_next = False
        for j in range(len(self) - 1):
            if j == i:
                self.array[j] = self.array[j + 1]
                is_next = True
                continue

            if is_next:
                if (j + 1) < len(self):
                    self.array[j] = self.array[j + 1]
            else:
                self.array[j] = self.array[j]

        self.count -= 1
