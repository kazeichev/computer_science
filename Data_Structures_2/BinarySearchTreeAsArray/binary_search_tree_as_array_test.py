import unittest
from binary_search_tree_as_array import aBST, GenerateBBSTArray


class AddKeyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = aBST(3)

    def test(self):
        self.assertEqual(15, len(self.tree.Tree))
        self.assertEqual(0, self.tree.AddKey(50))
        self.assertEqual(1, self.tree.AddKey(25))
        self.assertEqual(2, self.tree.AddKey(75))
        self.assertEqual(4, self.tree.AddKey(37))
        self.assertEqual(5, self.tree.AddKey(62))
        self.assertEqual(6, self.tree.AddKey(84))
        self.assertEqual(9, self.tree.AddKey(31))
        self.assertEqual(10, self.tree.AddKey(43))
        self.assertEqual(11, self.tree.AddKey(55))
        self.assertEqual(14, self.tree.AddKey(92))

        self.assertEqual(-1, self.tree.AddKey(100))
        self.assertEqual(10, self.tree.AddKey(43))
        self.assertEqual(0, self.tree.AddKey(50))


class FindKeyIndexTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = aBST(3)
        self.tree.AddKey(50)
        self.tree.AddKey(25)
        self.tree.AddKey(75)
        self.tree.AddKey(37)
        self.tree.AddKey(62)
        self.tree.AddKey(84)
        self.tree.AddKey(31)
        self.tree.AddKey(43)
        self.tree.AddKey(55)
        self.tree.AddKey(92)

    def test(self):
        self.assertEqual(0, self.tree.FindKeyIndex(50))
        self.assertEqual(14, self.tree.FindKeyIndex(92))
        self.assertEqual(2, self.tree.FindKeyIndex(75))

        self.assertIsNone(self.tree.FindKeyIndex(100))
        self.assertEqual(-3, self.tree.FindKeyIndex(24))


class FindKeyIndexInEmptyTreeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = aBST(3)

    def test(self):
        self.assertEqual(0, self.tree.FindKeyIndex(50))


class GenerateBBSTArrayTestCase(unittest.TestCase):
    def test(self):
        self.assertListEqual(
            [50, 25, 75, 20, 37, 62, 84, 19, 21, 31, 43, 55, 63, 81, 92],
            GenerateBBSTArray([81, 92, 55, 63, 31, 43, 84, 21, 19, 62, 37, 50, 25, 20, 75])
        )


class GenerateBBSTArrayFromEmptyListTestCase(unittest.TestCase):
    def test(self):
        self.assertIsNone(GenerateBBSTArray([]))
