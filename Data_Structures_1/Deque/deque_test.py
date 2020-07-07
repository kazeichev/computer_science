from deque import Deque
import unittest


class AddToEmptyDeque(unittest.TestCase):
    def setUp(self) -> None:
        self.d = Deque()

    def test_add_to_front(self):
        self.assertEqual(0, self.d.size())
        self.assertIsNone(self.d.removeFront())

        self.d.addFront(1)

        self.assertEqual(1, self.d.size())
        self.assertEqual(1, self.d.removeFront())

    def test_add_to_tail(self):
        self.assertEqual(0, self.d.size())
        self.assertIsNone(self.d.removeTail())

        self.d.addTail(1)

        self.assertEqual(1, self.d.size())
        self.assertEqual(1, self.d.removeTail())


class AddToNotEmptyDeque(unittest.TestCase):
    def setUp(self) -> None:
        self.d = Deque()
        for i in range(0, 6):
            self.d.addFront(i)

    def test_add_to_front(self):
        self.assertEqual(6, self.d.size())

        self.d.addFront(100)

        self.assertEqual(7, self.d.size())
        self.assertEqual(100, self.d.removeFront())
        self.assertEqual(6, self.d.size())

    def test_add_to_tail(self):
        self.assertEqual(6, self.d.size())

        self.d.addTail(100)

        self.assertEqual(7, self.d.size())
        self.assertEqual(100, self.d.removeTail())
        self.assertEqual(6, self.d.size())


class RemoveFromEmptyDeque(unittest.TestCase):
    def setUp(self) -> None:
        self.d = Deque()

    def test_remove_from_front(self):
        self.assertEqual(0, self.d.size())
        self.assertIsNone(self.d.removeFront())

    def test_remove_from_tail(self):
        self.assertEqual(0, self.d.size())
        self.assertIsNone(self.d.removeTail())


class RemoveFromNotEmptyDeque(unittest.TestCase):
    def setUp(self) -> None:
        self.d = Deque()
        for i in range(0, 6):
            self.d.addTail(i)

    def test_remove_from_front(self):
        self.assertEqual(6, self.d.size())

        for i in range(0, 6):
            self.assertEqual(i, self.d.removeFront())

    def test_remove_from_tail(self):
        self.assertEqual(6, self.d.size())

        for i in reversed(range(0, 6)):
            self.assertEqual(i, self.d.removeTail())


class SizeEmptyDeque(unittest.TestCase):
    def setUp(self) -> None:
        self.d = Deque()

    def test(self):
        self.assertEqual(0, self.d.size())


class SizeNotEmptyDeque(unittest.TestCase):
    def setUp(self) -> None:
        self.d = Deque()
        for i in range(0, 6):
            self.d.addTail(i)

    def test(self):
        self.assertEqual(6, self.d.size())


if __name__ == '__main__':
    unittest.main()
