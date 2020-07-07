class BloomFilter:
    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = [0] * f_len

    def hash1(self, str1):
        n = 0
        for c in str1:
            n = n * 17 + ord(c)

        return n % self.filter_len

    def hash2(self, str1):
        n = 0
        for c in str1:
            n = n * 223 + ord(c)

        return n % self.filter_len

    def add(self, str1):
        indexes = [self.hash1(str1), self.hash2(str1)]

        for index in indexes:
            self.filter[index] = 1

    def is_value(self, str1):
        indexes = [self.hash1(str1), self.hash2(str1)]

        for index in indexes:
            if self.filter[index] == 0:
                return False

        return True
