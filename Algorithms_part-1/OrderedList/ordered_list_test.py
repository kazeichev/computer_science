from ordered_list import OrderedList, Node, OrderedStringList
import unittest


class CompareTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ol = OrderedList(True)

    def test(self):
        self.assertEqual(+1, self.ol.compare(3, 1))
        self.assertEqual(+1, self.ol.compare(3, 0))
        self.assertEqual(+1, self.ol.compare(301, 100))
        self.assertEqual(-1, self.ol.compare(1, 3))
        self.assertEqual(-1, self.ol.compare(0, 3))
        self.assertEqual(-1, self.ol.compare(200, 300))
        self.assertEqual(0, self.ol.compare(0, 0))
        self.assertEqual(0, self.ol.compare(1, 1))
        self.assertEqual(0, self.ol.compare(300, 300))


class CompareStringsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ol = OrderedStringList(True)

    def test(self):
        self.assertEqual(-1, self.ol.compare("ааа", "яяя"))
        self.assertEqual(-1, self.ol.compare("абв", "язз"))
        self.assertEqual(+1, self.ol.compare("ячс", "асм"))
        self.assertEqual(0, self.ol.compare("ааа", "ааа"))
        self.assertEqual(0, self.ol.compare("яяя", "яяя"))
        self.assertEqual(0, self.ol.compare("", ""))


class AddToEmptyListTestCase(unittest.TestCase):
    def test_asc(self):
        self.ol = OrderedList(True)

        self.assertEqual(0, self.ol.len())
        self.assertIsNone(self.ol.head)
        self.assertIsNone(self.ol.tail)

        self.ol.add(1)

        self.assertEqual(1, self.ol.len())
        self.assertEqual(1, self.ol.head.value)
        self.assertEqual(1, self.ol.tail.value)
        self.assertEqual(1, self.ol.get_all()[0].value)

    def test_desc(self):
        self.ol = OrderedList(False)

        self.assertEqual(0, self.ol.len())
        self.assertIsNone(self.ol.head)
        self.assertIsNone(self.ol.tail)

        self.ol.add(1)

        self.assertEqual(1, self.ol.len())
        self.assertEqual(1, self.ol.head.value)
        self.assertEqual(1, self.ol.tail.value)
        self.assertEqual(1, self.ol.get_all()[0].value)


class AddToMiddleAscListTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ol = OrderedList(True)

        for i in range(0, 6):
            self.ol.add(i)

    def test(self):
        self.assertEqual(6, self.ol.len())
        self.assertEqual(0, self.ol.head.value)
        self.assertEqual(5, self.ol.tail.value)
        self.assertIsNone(self.ol.head.prev)
        self.assertIsNone(self.ol.tail.next)
        self.assertEqual(0, self.ol.head.next.prev.value)

        self.ol.add(4)

        nodes = []
        for i in self.ol.get_all():
            nodes.append(i.value)

        self.assertListEqual(nodes, [0, 1, 2, 3, 4, 4, 5])

        self.assertEqual(7, self.ol.len())
        self.assertEqual(0, self.ol.head.value)
        self.assertEqual(5, self.ol.tail.value)
        self.assertIsNone(self.ol.head.prev)
        self.assertIsNone(self.ol.tail.next)


class AddToMiddleDescListTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ol = OrderedList(False)
        for i in range(0, 6):
            self.ol.add(i)

    def test(self):
        self.assertEqual(6, self.ol.len())
        self.assertEqual(5, self.ol.head.value)
        self.assertEqual(4, self.ol.head.next.value)
        self.assertEqual(5, self.ol.head.next.prev.value)
        self.assertEqual(0, self.ol.tail.value)
        self.assertEqual(1, self.ol.tail.prev.value)
        self.assertEqual(0, self.ol.tail.prev.next.value)

        self.assertIsNone(self.ol.head.prev)
        self.assertIsNone(self.ol.tail.next)

        self.ol.add(4)

        nodes = []
        for i in self.ol.get_all():
            nodes.append(i.value)

        self.assertListEqual(nodes, [5, 4, 4, 3, 2, 1, 0])
        self.assertEqual(7, self.ol.len())
        self.assertEqual(5, self.ol.head.value)
        self.assertEqual(4, self.ol.head.next.value)
        self.assertEqual(5, self.ol.head.next.prev.value)
        self.assertEqual(0, self.ol.tail.value)
        self.assertEqual(1, self.ol.tail.prev.value)
        self.assertEqual(0, self.ol.tail.prev.next.value)

        self.assertIsNone(self.ol.head.prev)
        self.assertIsNone(self.ol.tail.next)


class AddToHeadAscListWithMultipleValuesTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ol = OrderedList(True)

        for i in range(1, 6):
            self.ol.add(i)

    def test(self):
        self.assertEqual(5, self.ol.len())
        self.assertEqual(1, self.ol.head.value)
        self.assertEqual(5, self.ol.tail.value)
        self.assertIsNone(self.ol.head.prev)
        self.assertIsNone(self.ol.tail.next)

        self.ol.add(0)

        self.assertEqual(6, self.ol.len())
        self.assertEqual(0, self.ol.head.value)
        self.assertEqual(5, self.ol.tail.value)
        self.assertIsNone(self.ol.head.prev)
        self.assertIsNone(self.ol.tail.next)
        self.assertEqual(1, self.ol.head.next.value)
        self.assertEqual(0, self.ol.head.next.prev.value)


class AddToHeadAscListWithSingleValueTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ol = OrderedList(True)
        self.ol.add(1)

    def test(self):
        self.assertEqual(1, self.ol.len())
        self.assertEqual(1, self.ol.head.value)
        self.assertEqual(1, self.ol.tail.value)
        self.assertIsNone(self.ol.head.prev)
        self.assertIsNone(self.ol.head.next)
        self.assertIsNone(self.ol.tail.next)
        self.assertIsNone(self.ol.tail.prev)

        self.ol.add(0)

        self.assertEqual(2, self.ol.len())
        self.assertEqual(0, self.ol.head.value)
        self.assertIsNone(self.ol.head.prev)
        self.assertEqual(1, self.ol.head.next.value)
        self.assertEqual(0, self.ol.head.next.prev.value)
        self.assertEqual(1, self.ol.tail.value)
        self.assertEqual(0, self.ol.tail.prev.value)
        self.assertIsNone(self.ol.tail.next)


class AddToEndAscListWithMultipleValuesTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ol = OrderedList(True)
        for i in range(0, 6):
            self.ol.add(i)

    def test(self):
        self.assertEqual(6, self.ol.len())
        self.assertEqual(0, self.ol.head.value)
        self.assertEqual(1, self.ol.head.next.value)
        self.assertIsNone(self.ol.head.prev)
        self.assertEqual(0, self.ol.head.next.prev.value)
        self.assertEqual(5, self.ol.tail.value)
        self.assertEqual(4, self.ol.tail.prev.value)
        self.assertEqual(5, self.ol.tail.prev.next.value)
        self.assertIsNone(self.ol.tail.next)

        self.ol.add(6)

        self.assertEqual(7, self.ol.len())
        self.assertEqual(0, self.ol.head.value)
        self.assertEqual(1, self.ol.head.next.value)
        self.assertIsNone(self.ol.head.prev)
        self.assertEqual(0, self.ol.head.next.prev.value)
        self.assertEqual(6, self.ol.tail.value)
        self.assertEqual(5, self.ol.tail.prev.value)
        self.assertEqual(6, self.ol.tail.prev.next.value)
        self.assertIsNone(self.ol.tail.next)


class AddToEndAscListWithSingleValueTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ol = OrderedList(True)
        self.ol.add(1)

    def test(self):
        self.assertEqual(1, self.ol.len())
        self.assertEqual(1, self.ol.head.value)
        self.assertEqual(1, self.ol.tail.value)

        self.assertIsNone(self.ol.head.prev)
        self.assertIsNone(self.ol.head.next)
        self.assertIsNone(self.ol.tail.prev)
        self.assertIsNone(self.ol.tail.next)

        self.ol.add(2)

        self.assertEqual(2, self.ol.len())
        self.assertEqual(1, self.ol.head.value)
        self.assertEqual(2, self.ol.head.next.value)
        self.assertEqual(1, self.ol.head.next.prev.value)
        self.assertEqual(2, self.ol.tail.value)
        self.assertEqual(1, self.ol.tail.prev.value)
        self.assertEqual(2, self.ol.tail.prev.next.value)

        self.assertIsNone(self.ol.head.prev)
        self.assertIsNone(self.ol.tail.next)


class FindDescTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ol = OrderedList(False)
        for i in range(0, 6):
            self.ol.add(i)

    def test(self):
        self.assertIsInstance(self.ol.find(0), Node)
        self.assertIsInstance(self.ol.find(5), Node)
        self.assertIsInstance(self.ol.find(3), Node)

    def test_empty(self):
        self.ol = OrderedList(False)
        self.assertIsNone(self.ol.find(0))


class FindAscTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ol = OrderedList(True)
        for i in range(0, 6):
            self.ol.add(i)

    def test(self):
        self.assertIsInstance(self.ol.find(0), Node)
        self.assertIsInstance(self.ol.find(5), Node)
        self.assertIsInstance(self.ol.find(3), Node)

    def test_empty(self):
        self.ol = OrderedList(True)
        self.assertIsNone(self.ol.find(3))


class DeleteFromAscListWithSingleValueTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ol = OrderedList(True)
        self.ol.add(1)

    def test(self):
        self.assertEqual(1, self.ol.len())
        self.assertEqual(1, self.ol.head.value)
        self.assertEqual(1, self.ol.tail.value)

        self.assertIsNone(self.ol.head.prev)
        self.assertIsNone(self.ol.head.next)
        self.assertIsNone(self.ol.tail.next)
        self.assertIsNone(self.ol.tail.prev)

        self.ol.delete(1)

        self.assertEqual(0, self.ol.len())
        self.assertIsNone(self.ol.head)
        self.assertIsNone(self.ol.tail)


class DeleteFromHeadAscListWithMultipleValuesTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ol = OrderedList(True)
        for i in range(0, 6):
            self.ol.add(i)

    def test(self):
        self.assertEqual(6, self.ol.len())
        self.assertEqual(0, self.ol.head.value)
        self.assertEqual(1, self.ol.head.next.value)

        self.assertIsNone(self.ol.head.prev)

        self.ol.delete(0)

        self.assertEqual(5, self.ol.len())
        self.assertEqual(1, self.ol.head.value)
        self.assertEqual(2, self.ol.head.next.value)
        self.assertEqual(1, self.ol.head.next.prev.value)

        self.assertIsNone(self.ol.head.prev)


class DeleteFromEndAscListWithMultipleValuesTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ol = OrderedList(True)
        for i in range(0, 6):
            self.ol.add(i)

    def test(self):
        self.assertEqual(6, self.ol.len())
        self.assertEqual(5, self.ol.tail.value)
        self.assertEqual(4, self.ol.tail.prev.value)
        self.assertEqual(5, self.ol.tail.prev.next.value)

        self.assertIsNone(self.ol.tail.next)

        self.ol.delete(5)

        self.assertEqual(5, self.ol.len())
        self.assertEqual(4, self.ol.tail.value)
        self.assertEqual(3, self.ol.tail.prev.value)
        self.assertEqual(4, self.ol.tail.prev.next.value)

        self.assertIsNone(self.ol.tail.next)


class DeleteFromMiddleDescListWithMultipleValuesTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ol = OrderedList(False)
        for i in range(0, 6):
            self.ol.add(i)

    def test(self):
        self.assertEqual(6, self.ol.len())

        nodes = []
        for i in self.ol.get_all():
            nodes.append(i.value)

        self.assertListEqual(nodes, [5, 4, 3, 2, 1, 0])

        self.ol.delete(3)

        self.assertEqual(5, self.ol.len())

        nodes = []
        for i in self.ol.get_all():
            nodes.append(i.value)

        self.assertListEqual(nodes, [5, 4, 2, 1, 0])

        node_4 = self.ol.find(4)
        node_2 = self.ol.find(2)

        self.assertEqual(node_2, node_4.next)
        self.assertEqual(node_4, node_2.prev)


if __name__ == '__main__':
    unittest.main()
