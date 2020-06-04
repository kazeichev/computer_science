import unittest
from stack import Stack


class PushToEmptyStackTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Stack()

    def test(self):
        self.assertEqual(0, self.s.size())
        self.s.push(1)

        self.assertEqual(1, self.s.size())


class PushToStackWithSingleValueTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Stack()
        self.s.push(1)

    def test(self):
        self.assertEqual(1, self.s.size())
        self.s.push(2)

        self.assertEqual(2, self.s.size())


class PushToStackWithMultipleValuesTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Stack()
        for i in range(30):
            self.s.push(i)

    def test(self):
        self.assertEqual(30, self.s.size())
        self.s.push(100)

        self.assertEqual(31, self.s.size())


class PopFromEmptyStackTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Stack()

    def test(self):
        self.assertEqual(0, self.s.size())
        self.assertIsNone(self.s.pop())


class PopFromStackWithSingleValueTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Stack()
        self.s.push(1)

    def test(self):
        self.assertEqual(1, self.s.size())

        self.s.pop()

        self.assertEqual(0, self.s.size())


class PopFromStackWithMultipleValuesTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Stack()
        for i in range(30):
            self.s.push(i)

    def test(self):
        self.assertEqual(30, self.s.size())

        self.s.pop()

        self.assertEqual(29, self.s.size())

    def test_multiple(self):
        self.assertEqual(30, self.s.size())

        while self.s.size() > 0:
            self.s.pop()

        self.assertEqual(0, self.s.size())


class SizeEmptyStackTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Stack()

    def test(self):
        self.assertEqual(0, self.s.size())


class SizeStackWithMultipleValuesTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Stack()
        for i in range(30):
            self.s.push(i)

    def test(self):
        self.assertEqual(30, self.s.size())


class PeekEmptyStackTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Stack()

    def test(self):
        self.assertEqual(0, self.s.size())
        self.assertIsNone(self.s.peek())


class PeekFromStackWithSingleValueTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Stack()
        self.s.push(1)

    def test(self):
        self.assertEqual(1, self.s.size())
        self.assertEqual(1, self.s.peek())
        self.assertEqual(1, self.s.size())


class PeekFromStackWithMultipleValuesTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Stack()
        for i in range(30):
            self.s.push(i)

    def test(self):
        self.assertEqual(30, self.s.size())
        self.assertEqual(29, self.s.peek())
        self.assertEqual(30, self.s.size())


if __name__ == '__main__':
    unittest.main()
