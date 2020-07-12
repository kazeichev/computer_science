import unittest
from binary_search_tree import BST, BSTNode


class BaseBinarySearchTreeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BST(None)
        self.tree.AddKeyValue(4, "value_4")
        self.tree.AddKeyValue(2, "value_2")
        self.tree.AddKeyValue(1, "value_1")
        self.tree.AddKeyValue(3, "value_3")
        self.tree.AddKeyValue(6, "value_6")
        self.tree.AddKeyValue(5, "value_5")
        self.tree.AddKeyValue(7, "value_7")


class AddKeyValueToEmptyTreeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BST(None)

    def test(self):
        self.assertIsNone(self.tree.Root)
        self.assertFalse(self.tree.FindNodeByKey(4).NodeHasKey)
        self.tree.AddKeyValue(4, "value_4")

        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual("value_4", self.tree.Root.NodeValue)
        self.assertIsNone(self.tree.Root.Parent)
        self.assertIsNone(self.tree.Root.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild)


class AddKeyValueToNotEmptyTreeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BST(None)
        self.tree.AddKeyValue(4, "value_4")
        self.tree.AddKeyValue(2, "value_2")
        self.tree.AddKeyValue(6, "value_6")

    def test_left(self):
        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(2, self.tree.Root.LeftChild.NodeKey)
        self.assertEqual(6, self.tree.Root.RightChild.NodeKey)
        self.assertFalse(self.tree.FindNodeByKey(1).NodeHasKey)

        self.tree.AddKeyValue(1, "value_1")
        self.assertEqual(2, self.tree.Root.LeftChild.NodeKey)
        self.assertEqual(4, self.tree.Root.LeftChild.Parent.NodeKey)
        self.assertEqual(1, self.tree.Root.LeftChild.LeftChild.NodeKey)
        self.assertEqual(2, self.tree.Root.LeftChild.LeftChild.Parent.NodeKey)

    def test_right(self):
        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(2, self.tree.Root.LeftChild.NodeKey)
        self.assertEqual(6, self.tree.Root.RightChild.NodeKey)
        self.assertFalse(self.tree.FindNodeByKey(7).NodeHasKey)

        self.tree.AddKeyValue(7, "value_7")
        self.assertEqual(6, self.tree.Root.RightChild.NodeKey)
        self.assertEqual(4, self.tree.Root.RightChild.Parent.NodeKey)
        self.assertEqual(7, self.tree.Root.RightChild.RightChild.NodeKey)
        self.assertEqual(6, self.tree.Root.RightChild.RightChild.Parent.NodeKey)


class AddExistingKeyValueToNotEmptyTreeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BST(None)
        self.tree.AddKeyValue(4, "value_4")
        self.tree.AddKeyValue(2, "value_2")
        self.tree.AddKeyValue(6, "value_6")

    def test(self):
        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(2, self.tree.Root.LeftChild.NodeKey)
        self.assertEqual(6, self.tree.Root.RightChild.NodeKey)

        self.assertTrue(self.tree.FindNodeByKey(6).NodeHasKey)
        self.assertTrue(self.tree.FindNodeByKey(2).NodeHasKey)

        self.assertFalse(self.tree.AddKeyValue(6, "value_6"))
        self.assertFalse(self.tree.AddKeyValue(2, "value_2"))


class FindInEmptyTreeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BST(None)

    def test(self):
        self.assertIsNone(self.tree.Root)
        self.assertIsNone(self.tree.FindNodeByKey(4).Node)
        self.assertFalse(self.tree.FindNodeByKey(4).NodeHasKey)


class FindInTreeTestCase(BaseBinarySearchTreeTestCase):
    def test(self):
        self.assertTrue(self.tree.FindNodeByKey(4).NodeHasKey)
        self.assertTrue(self.tree.FindNodeByKey(1).NodeHasKey)
        self.assertTrue(self.tree.FindNodeByKey(5).NodeHasKey)
        self.assertTrue(self.tree.FindNodeByKey(7).NodeHasKey)
        self.assertTrue(self.tree.FindNodeByKey(3).NodeHasKey)
        self.assertTrue(self.tree.FindNodeByKey(2).NodeHasKey)
        self.assertTrue(self.tree.FindNodeByKey(6).NodeHasKey)

        self.assertEqual(7, self.tree.FindNodeByKey(7).Node.NodeKey)
        self.assertFalse(self.tree.FindNodeByKey(7).Node.ToLeft)
        self.assertFalse(self.tree.FindNodeByKey(7).Node.NodeHasKey)

        self.assertEqual(1, self.tree.FindNodeByKey(0).Node.NodeKey)
        self.assertTrue(self.tree.FindNodeByKey(0).Node.ToLeft)
        self.assertFalse(self.tree.FindNodeByKey(0).Node.NodeHasKey)


class FindMinMaxInEmptyTreeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BST(None)

    def test(self):
        self.assertIsNone(self.tree.Root)
        self.assertIsNone(self.tree.FinMinMax(None, True))


class FindMinKeyInTreeTestCase(BaseBinarySearchTreeTestCase):
    def test(self):
        self.assertEqual(4, self.tree.Root.NodeKey)

        self.assertEqual(1, self.tree.FinMinMax(self.tree.Root, False))
        self.assertEqual(1, self.tree.FinMinMax(self.tree.Root.LeftChild, False))
        self.assertEqual(1, self.tree.FinMinMax(self.tree.Root.LeftChild.LeftChild, False))
        self.assertEqual(5, self.tree.FinMinMax(self.tree.Root.RightChild, False))


class FindMaxKeyInTreeTestCase(BaseBinarySearchTreeTestCase):
    def test(self):
        self.assertEqual(4, self.tree.Root.NodeKey)

        self.assertEqual(7, self.tree.FinMinMax(self.tree.Root), True)
        self.assertEqual(7, self.tree.FinMinMax(self.tree.Root.RightChild), True)
        self.assertEqual(7, self.tree.FinMinMax(self.tree.Root.RightChild.RightChild), True)
        self.assertEqual(3, self.tree.FinMinMax(self.tree.Root.LeftChild), True)


class RemoveFromEmptyTreeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BST(None)

    def test(self):
        self.assertIsNone(self.tree.Root)
        self.assertFalse(self.tree.DeleteNodeByKey(4))


class RemoveLeftNotLeafNodeTestCase(BaseBinarySearchTreeTestCase):
    def test(self):
        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(2, self.tree.Root.LeftChild.NodeKey)

        self.tree.DeleteNodeByKey(2)
        self.assertEqual(3, self.tree.Root.LeftChild.NodeKey)
        self.assertEqual(4, self.tree.Root.LeftChild.Parent.NodeKey)
        self.assertEqual(1, self.tree.Root.LeftChild.LeftChild.NodeKey)
        self.assertIsNone(self.tree.Root.LeftChild.RightChild)
        self.assertFalse(self.tree.FindNodeByKey(2))


class RemoveRightNotLeafNodeTestCase(BaseBinarySearchTreeTestCase):
    def test(self):
        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(6, self.tree.Root.RightChild.NodeKey)

        self.tree.DeleteNodeByKey(6)
        self.assertEqual(7, self.tree.Root.RightChild.NodeKey)
        self.assertEqual(4, self.tree.Root.RightChild.Parent.NodeKey)
        self.assertEqual(5, self.tree.Root.RightChild.LeftChild.NodeKey)
        self.assertIsNone(self.tree.Root.RightChild.RightChild)
        self.assertFalse(self.tree.FindNodeByKey(6))


class RemoveLeftLeafNodeTestCase(BaseBinarySearchTreeTestCase):
    def test(self):
        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(2, self.tree.Root.LeftChild.NodeKey)
        self.assertEqual(1, self.tree.Root.LeftChild.LeftChild.NodeKey)

        self.tree.DeleteNodeByKey(1)

        self.assertEqual(2, self.tree.Root.LeftChild.NodeKey)
        self.assertIsNone(self.tree.Root.LeftChild.LeftChild)
        self.assertEqual(3, self.tree.Root.LeftChild.RightChild.NodeKey)
        self.assertFalse(self.tree.FindNodeByKey(1))


class RemoveRightLeafNodeTestCase(BaseBinarySearchTreeTestCase):
    def test(self):
        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(6, self.tree.Root.RightChild.NodeKey)
        self.assertEqual(7, self.tree.Root.RightChild.RightChild.NodeKey)

        self.tree.DeleteNodeByKey(7)

        self.assertEqual(6, self.tree.Root.RightChild.NodeKey)
        self.assertIsNone(self.tree.Root.RightChild.RightChild)
        self.assertEqual(5, self.tree.Root.RightChild.LeftChild.NodeKey)
        self.assertFalse(self.tree.FindNodeByKey(7))


class RemoveFromAdvanceTreeTestCase(BaseBinarySearchTreeTestCase):
    def test(self):
        self.tree.AddKeyValue(10, "value_10")
        self.tree.AddKeyValue(11, "value_11")
        self.tree.AddKeyValue(9, "value_9")
        self.tree.AddKeyValue(8, "value_8")

        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(6, self.tree.Root.RightChild.NodeKey)
        self.assertEqual(7, self.tree.Root.RightChild.RightChild.NodeKey)
        self.assertEqual(10, self.tree.Root.RightChild.RightChild.RightChild.NodeKey)
        self.assertEqual(11, self.tree.Root.RightChild.RightChild.RightChild.RightChild.NodeKey)
        self.assertEqual(9, self.tree.Root.RightChild.RightChild.RightChild.LeftChild.NodeKey)
        self.assertEqual(8, self.tree.Root.RightChild.RightChild.RightChild.LeftChild.LeftChild.NodeKey)
        self.assertTrue(self.tree.FindNodeByKey(7))

        self.tree.DeleteNodeByKey(7)
        self.assertFalse(self.tree.FindNodeByKey(7))
        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(6, self.tree.Root.RightChild.NodeKey)
        self.assertEqual(8, self.tree.Root.RightChild.RightChild.NodeKey)
        self.assertEqual(10, self.tree.Root.RightChild.RightChild.RightChild.NodeKey)
        self.assertEqual(11, self.tree.Root.RightChild.RightChild.RightChild.RightChild.NodeKey)
        self.assertEqual(9, self.tree.Root.RightChild.RightChild.RightChild.LeftChild.NodeKey)
        self.assertIsNone(self.tree.Root.RightChild.RightChild.RightChild.LeftChild.LeftChild.NodeKey)


class CountNotEmptyTreeTestCase(BaseBinarySearchTreeTestCase):
    def test(self):
        self.assertEqual(7, self.tree.Count())
        self.assertNotEqual(1, self.tree.Count())


class CountEmptyTreeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BST(None)

    def test(self):
        self.assertIsNone(self.tree.Root)
        self.assertEqual(0, self.tree.Count())


if __name__ == '__main__':
    unittest.main()
