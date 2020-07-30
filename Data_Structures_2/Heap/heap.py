class Heap:
    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def get_parent(self, index):
        return int((index - 1) // 2)

    def has_parent(self, index):
        return self.get_parent(index) >= 0

    def get_left_child(self, index):
        return 2 * index + 1

    def get_right_child(self, index):
        return 2 * index + 2

    def has_any_children(self, index):
        return (self.get_left_child(index) < len(self.HeapArray) and self.HeapArray[
            self.get_left_child(index)] is not None) \
               or (self.get_right_child(index) < len(self.HeapArray) and self.HeapArray[
            self.get_right_child(index)] is not None)

    def MakeHeap(self, a, depth):
        """
        создаём массив кучи HeapArray из заданного
        размер массива выбираем на основе глубины depth
        :param a:
        :param depth:
        :return:
        """
        self.HeapArray = [None] * (pow(2, depth + 1) - 1)
        for i in a:
            self.Add(i)

    def GetMax(self):
        """
        вернуть значение корня и перестроить кучу
        :return: -1 если куча пуста
        """
        if len(self.HeapArray) == 0 or self.HeapArray[0] is None:
            return -1

        last = self.HeapArray.index(next((x for x in reversed(self.HeapArray) if x is not None), None))
        result = self.HeapArray[0]

        self.HeapArray[0], self.HeapArray[last] = self.HeapArray[last], self.HeapArray[0]
        self.HeapArray[last] = None
        self.heapify_down()

        return result

    def heapify_down(self):
        index = 0
        while self.has_any_children(index):
            left = self.get_left_child(index)
            right = self.get_right_child(index)
            max_child = index

            if self.HeapArray[left] is not None and self.HeapArray[right] is not None:
                if self.HeapArray[left] > self.HeapArray[right]:
                    max_child = left
                else:
                    max_child = right
            elif self.HeapArray[left] is not None and self.HeapArray[right] is None:
                max_child = left
            elif self.HeapArray[left] is None and self.HeapArray[right] is not None:
                max_child = right

            if self.HeapArray[max_child] > self.HeapArray[index]:
                self.HeapArray[max_child], self.HeapArray[index] = self.HeapArray[index], self.HeapArray[max_child]
            index = max_child

    def heapify_up(self, index):
        """
        :param index:
        :return:
        """
        while self.has_parent(index) and self.HeapArray[index] > self.HeapArray[self.get_parent(index)]:
            self.HeapArray[index], self.HeapArray[self.get_parent(index)] = self.HeapArray[self.get_parent(index)], \
                                                                            self.HeapArray[index]
            index = self.get_parent(index)

    def Add(self, key):
        """
        добавляем новый элемент key в кучу и перестраиваем её
        :param key:
        :return:  False если куча вся заполнена
        """
        index = 0
        for i in self.HeapArray:
            if i is None:
                index = self.HeapArray.index(i)

        if None not in self.HeapArray:
            return False

        self.HeapArray[index] = key
        self.heapify_up(index)
        return True
