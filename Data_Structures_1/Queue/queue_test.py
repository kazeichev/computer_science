from queue import Queue
import unittest


class EnqueueInEmptyQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.q = Queue()

    def test(self):
        self.assertEqual(0, self.q.size())
        self.q.enqueue(1)
        self.assertEqual(1, self.q.size())
        self.assertEqual(1, self.q.dequeue())


class EnqueueInNotEmptyQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.q = Queue()
        for i in range(0, 10):
            self.q.enqueue(i)

    def test(self):
        self.assertEqual(10, self.q.size())
        self.q.enqueue(10)
        self.assertEqual(11, self.q.size())

        for i in range(0, 11):
            self.assertEqual(i, self.q.dequeue())


class DequeueFromEmptyQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.q = Queue()

    def test(self):
        self.assertEqual(0, self.q.size())
        self.assertIsNone(self.q.dequeue())


class DequeueFromNotEmptyQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.q = Queue()
        for i in range(0, 10):
            self.q.enqueue(i)

    def test(self):
        self.assertEqual(10, self.q.size())

        for i in range(0, 10):
            self.assertEqual(i, self.q.dequeue())

        self.assertEqual(0, self.q.size())
        self.assertIsNone(self.q.dequeue())


class SizeOfEmptyQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.q = Queue()

    def test(self):
        self.assertEqual(0, self.q.size())


class SizeOfNotEmptyQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.q = Queue()
        for i in range(0, 10):
            self.q.enqueue(i)

    def test(self):
        self.assertEqual(10, self.q.size())


if __name__ == '__main__':
    unittest.main()
