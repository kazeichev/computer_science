class aBST:
    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = pow(2, depth + 1) - 1
        self.Tree = [None] * tree_size  # массив ключей

    def FindKeyIndex(self, key):
        """
        ищем в массиве индекс ключа
        :param key:
        :return: None - не найден|index
        """
        index = 0
        if self.Tree[index] is None:
            return index

        while self.Tree[index] is not None:
            if key < self.Tree[index]:
                index = 2 * index + 1
            elif key > self.Tree[index]:
                index = 2 * index + 2
            elif self.Tree[index] == key:
                break

            if index >= len(self.Tree):
                return None

            if self.Tree[index] is None:
                return -index

        return index

    def AddKey(self, key):
        """
        добавляем ключ в массив
        :param key:
        :return: индекс добавленного/существующего ключа или -1 если не удалось
        """
        index = 0
        if self.Tree[index] is None:
            self.Tree[index] = key
            return index

        while self.Tree[index] is not None:
            if key < self.Tree[index]:
                index = 2 * index + 1
            elif key > self.Tree[index]:
                index = 2 * index + 2
            elif self.Tree[index] == key:
                return index

            if index >= len(self.Tree):
                return -1

        self.Tree[index] = key
        return index
