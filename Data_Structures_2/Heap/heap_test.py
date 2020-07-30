import unittest
from heap import Heap


class GenerateHeapTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.h = Heap()

    def test(self):
        self.assertEqual(0, len(self.h.HeapArray))
        self.h.MakeHeap([7, 3, 2, 6, 5, 1, 4, 11, 9, 8, 10, 0, 15, 12, 20], 3)

        self.assertListEqual([20, 10, 15, 7, 9, 4, 12, 3, 6, 5, 8, 0, 1, 2, 11], self.h.HeapArray)
        self.assertFalse(self.h.Add(100))


class AddKeyToEmptyHeapTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.h = Heap()
        self.h.MakeHeap([], 3)

    def test(self):
        self.assertIsNone(self.h.HeapArray[0])
        self.assertTrue(self.h.Add(0))
        self.assertEqual(0, self.h.HeapArray[0])


class GetMaxFromEmptyHeapTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.h = Heap()

    def test(self):
        self.assertEqual(-1, self.h.GetMax())


class GetMapFromHeapWithSingleKeyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.h = Heap()
        self.h.MakeHeap([11], 1)

    def test(self):
        self.assertEqual(11, self.h.GetMax())
        self.assertIsNone(self.h.HeapArray[0])


class GetMapFromHeapTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.h = Heap()
        self.h.MakeHeap([7, 3, 2, 6, 5, 1, 4, 11, 9, 8], 3)

    def test(self):
        self.assertEqual(11, self.h.GetMax())
        self.assertEqual(9, self.h.HeapArray[0])
        self.assertIsNone(self.h.HeapArray[9])

