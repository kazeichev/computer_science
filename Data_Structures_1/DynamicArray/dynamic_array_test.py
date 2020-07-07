import unittest
from dynamic_array import DynArray


class InsertAtStartTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.da = DynArray()
        for i in range(1, 20):
            self.da.append(i)

    def test(self):
        self.assertEqual(32, self.da.capacity)
        self.assertEqual(19, self.da.count)

        self.da.insert(0, 21)

        self.assertEqual(21, self.da[0])
        self.assertEqual(1, self.da[1])
        self.assertEqual(20, len(self.da))
        self.assertEqual(32, self.da.capacity)


class InsertAtMiddleTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.da = DynArray()
        for i in range(1, 5):
            self.da.append(i)

    def test(self):
        self.assertEqual(16, self.da.capacity)
        self.assertEqual(4, self.da.count)

        self.da.insert(2, 100)

        self.assertEqual(100, self.da[2])
        self.assertEqual(2, self.da[1])
        self.assertEqual(3, self.da[3])
        self.assertEqual(5, len(self.da))
        self.assertEqual(16, self.da.capacity)


class InsertAtEndTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.da = DynArray()
        for i in range(1, 17):
            self.da.append(i)

    def test(self):
        self.assertEqual(16, self.da.capacity)
        self.assertEqual(16, self.da.count)
        self.assertEqual(16, len(self.da))
        self.assertEqual(16, self.da[15])

        self.da.insert(16, 17)

        self.assertEqual(17, self.da[16])
        self.assertEqual(32, self.da.capacity)
        self.assertEqual(17, self.da.count)


class InsertAtBadPositionTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.da = DynArray()
        for i in range(1, 17):
            self.da.append(i)

    def test_more(self):
        self.assertEqual(16, self.da.capacity)
        self.assertEqual(16, self.da.count)

        self.assertRaises(IndexError, self.da.insert, 17, 100)
        self.assertEqual(16, self.da.capacity)
        self.assertEqual(16, self.da.count)

    def test_less(self):
        self.assertEqual(16, self.da.capacity)
        self.assertEqual(16, self.da.count)

        self.assertRaises(IndexError, self.da.insert, -1, 100)
        self.assertEqual(16, self.da.capacity)
        self.assertEqual(16, self.da.count)


class InsertInEmptyArrayTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.da = DynArray()

    def test(self):
        self.assertEqual(0, self.da.count)
        self.assertEqual(0, len(self.da))

        self.da.insert(0, 1)

        self.assertEqual(1, self.da.count)
        self.assertEqual(16, self.da.capacity)
        self.assertEqual(1, self.da[0])


class InsertMultipleTimesTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.da = DynArray()
        for i in range(1, 17):
            self.da.append(i)

    def test(self):
        self.assertEqual(16, self.da.capacity)
        self.assertEqual(16, self.da.count)

        for i in range(16, 21):
            self.da.insert(i, i + 1)

        self.assertEqual(32, self.da.capacity)
        self.assertEqual(21, self.da.count)
        self.assertEqual(21, self.da[20])


class InsertWithCapacityModifyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.da = DynArray()
        for i in range(32):
            self.da.append(i)

    def test(self):
        self.assertEqual(32, self.da.capacity)
        self.assertEqual(32, self.da.count)

        self.da.insert(16, 100)
        self.da.insert(33, 200)

        self.assertEqual(64, self.da.capacity)
        self.assertEqual(34, self.da.count)
        self.assertEqual(200, self.da[33])


class DeleteFromEmptyArrayTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.da = DynArray()

    def test(self):
        self.assertEqual(0, self.da.count)
        self.assertEqual(0, len(self.da))

        self.assertRaises(IndexError, self.da.delete, 0)

        self.assertEqual(0, self.da.count)
        self.assertEqual(0, len(self.da))


class DeleteFromStartTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.da = DynArray()
        for i in range(1, 17):
            self.da.append(i)

    def test(self):
        self.assertEqual(16, self.da.capacity)
        self.assertEqual(16, self.da.count)

        self.da.delete(0)

        self.assertEqual(16, self.da.capacity)
        self.assertEqual(15, self.da.count)
        self.assertEqual(2, self.da[0])


class DeleteFromMiddleTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.da = DynArray()
        for i in range(1, 17):
            self.da.append(i)

    def test(self):
        self.assertEqual(16, self.da.capacity)
        self.assertEqual(16, self.da.count)
        self.assertEqual(15, self.da[14])

        self.da.delete(14)

        self.assertEqual(16, self.da.capacity)
        self.assertEqual(15, self.da.count)
        self.assertEqual(16, self.da[14])


class DeleteFromEndTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.da = DynArray()
        for i in range(1, 17):
            self.da.append(i)

    def test(self):
        self.assertEqual(16, self.da.capacity)
        self.assertEqual(16, self.da.count)
        self.assertEqual(16, self.da[15])

        self.da.delete(15)

        self.assertEqual(16, self.da.capacity)
        self.assertEqual(15, self.da.count)
        self.assertEqual(15, self.da[14])


class DeleteWithModifyCapacityTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.da = DynArray()
        for i in range(1, 18):
            self.da.append(i)

    def test(self):
        self.assertEqual(32, self.da.capacity)
        self.assertEqual(17, self.da.count)

        self.da.delete(15)
        self.da.delete(14)

        self.assertEqual(32, self.da.capacity)
        self.assertEqual(15, self.da.count)


class DeleteAtBadPositionTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.da = DynArray()
        for i in range(1, 17):
            self.da.append(i)

    def test_more(self):
        self.assertEqual(16, self.da.capacity)
        self.assertEqual(16, self.da.count)

        self.assertRaises(IndexError, self.da.delete, 17)
        self.assertEqual(16, self.da.capacity)
        self.assertEqual(16, self.da.count)

    def test_less(self):
        self.assertEqual(16, self.da.capacity)
        self.assertEqual(16, self.da.count)

        self.assertRaises(IndexError, self.da.delete, -1)
        self.assertEqual(16, self.da.capacity)
        self.assertEqual(16, self.da.count)


class DeleteMultipleTimesFromArray(unittest.TestCase):
    def setUp(self) -> None:
        self.da = DynArray()
        for i in range(32):
            self.da.append(i)

    def test(self):
        self.assertEqual(32, self.da.capacity)
        self.assertEqual(32, self.da.count)

        for i in reversed(range(len(self.da))):
            self.da.delete(i)

        self.assertEqual(0, self.da.count)
        self.assertEqual(16, self.da.capacity)


if __name__ == '__main__':
    unittest.main()
