import unittest
import random
import string
from hash_table import HashTable


class HashFuncTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.h = HashTable(19, 3)

    def test(self):
        i = 0
        while i < 1000000:
            index = self.h.hash_fun(''.join(random.choices(string.ascii_uppercase + string.digits, k=i)))
            self.assertTrue(0 <= index <= len(self.h.slots))
            i += 1


if __name__ == '__main__':
    unittest.main()
