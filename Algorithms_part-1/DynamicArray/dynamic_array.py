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

        if len(self) == i:
            self.append(itm)
            return

        tmp_array = self.make_array(self.capacity - i)
        for j in range(len(self) - i):
            tmp_array[j] = self.array[i + j]

        self.array[i] = itm
        for j in range(len(self) - i):
            self.array[j + i + 1] = tmp_array[j]

        self.count += 1

    def delete(self, i):
        if len(self) == 0:
            raise IndexError("Incorrect index")

        if i > len(self) or i < 0:
            raise IndexError("Incorrect index")

        self.count -= 1
        is_next = False
        for j in range(len(self)):
            if j == i:
                self.array[j] = self.array[j + 1]
                is_next = True
                continue

            if is_next:
                if (j + 1) < len(self):
                    self.array[j] = self.array[j + 1]
            else:
                self.array[j] = self.array[j]

        if len(self) < self.capacity // 2 and self.capacity > 16:
            self.resize(int(self.capacity // 1.5))
