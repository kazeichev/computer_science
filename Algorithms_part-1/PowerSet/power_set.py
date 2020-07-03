class PowerSet:
    def __init__(self):
        self.set = []

    def size(self):
        return len(self.set)

    def put(self, value):
        if self.get(value):
            return

        self.set.append(value)
        self.set.sort()

    def get(self, value):
        return value in self.set

    def remove(self, value):
        if self.get(value) is not True:
            return False

        self.set.remove(value)
        return True

    def intersection(self, set2):
        # пересечение текущего множества и set2
        new_set = PowerSet()

        for i in self.set:
            for j in set2.set:
                if i == j:
                    new_set.put(i)

        return new_set

    def union(self, set2):
        new_set = PowerSet()

        for i in self.set + set2.set:
            new_set.put(i)

        return new_set

    def difference(self, set2):
        new_set = PowerSet()

        for i in self.set:
            if i not in set2.set:
                new_set.put(i)

        return new_set

    def issubset(self, set2):
        for i in set2.set:
            if i not in self.set:
                return False

        return True
