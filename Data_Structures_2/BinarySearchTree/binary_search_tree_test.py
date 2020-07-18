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

        self.assertEqual(7, self.tree.FindNodeByKey(10).Node.NodeKey)
        self.assertFalse(self.tree.FindNodeByKey(10).ToLeft)
        self.assertFalse(self.tree.FindNodeByKey(10).NodeHasKey)

        self.assertEqual(1, self.tree.FindNodeByKey(0).Node.NodeKey)
        self.assertTrue(self.tree.FindNodeByKey(0).ToLeft)
        self.assertFalse(self.tree.FindNodeByKey(0).NodeHasKey)


class FindMinMaxInEmptyTreeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BST(None)

    def test(self):
        self.assertIsNone(self.tree.Root)
        self.assertIsNone(self.tree.FinMinMax(None, True))


class FindMinKeyInTreeTestCase(BaseBinarySearchTreeTestCase):
    def test(self):
        self.assertEqual(4, self.tree.Root.NodeKey)

        self.assertEqual(1, self.tree.FinMinMax(self.tree.Root, False).NodeKey)
        self.assertEqual(1, self.tree.FinMinMax(self.tree.Root.LeftChild, False).NodeKey)
        self.assertEqual(1, self.tree.FinMinMax(self.tree.Root.LeftChild.LeftChild, False).NodeKey)
        self.assertEqual(5, self.tree.FinMinMax(self.tree.Root.RightChild, False).NodeKey)


class FindMaxKeyInTreeTestCase(BaseBinarySearchTreeTestCase):
    def test(self):
        self.assertEqual(4, self.tree.Root.NodeKey)

        self.assertEqual(7, self.tree.FinMinMax(self.tree.Root, True).NodeKey)
        self.assertEqual(7, self.tree.FinMinMax(self.tree.Root.RightChild, True).NodeKey)
        self.assertEqual(7, self.tree.FinMinMax(self.tree.Root.RightChild.RightChild, True).NodeKey)
        self.assertEqual(3, self.tree.FinMinMax(self.tree.Root.LeftChild, True).NodeKey)


class RemoveFromEmptyTreeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BST(None)

    def test(self):
        self.assertIsNone(self.tree.Root)
        self.assertFalse(self.tree.DeleteNodeByKey(4))


class RemoveLeftNotLeafNodeWithLeftChildTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BST(None)
        self.tree.AddKeyValue(4, "value_4")
        self.tree.AddKeyValue(2, "value_2")
        self.tree.AddKeyValue(6, "value_6")
        self.tree.AddKeyValue(1, "value_1")

    def test(self):
        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(2, self.tree.Root.LeftChild.NodeKey)
        self.assertEqual(1, self.tree.Root.LeftChild.LeftChild.NodeKey)

        self.tree.DeleteNodeByKey(2)
        self.assertEqual(4, self.tree.Root.LeftChild.Parent.NodeKey)
        self.assertEqual(1, self.tree.Root.LeftChild.NodeKey)
        self.assertIsNone(self.tree.Root.LeftChild.RightChild)
        self.assertIsNone(self.tree.Root.LeftChild.LeftChild)
        self.assertFalse(self.tree.FindNodeByKey(2).NodeHasKey)


class RemoveLeftNotLeafNodeWithRightChildTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BST(None)
        self.tree.AddKeyValue(4, "value_4")
        self.tree.AddKeyValue(2, "value_2")
        self.tree.AddKeyValue(6, "value_6")
        self.tree.AddKeyValue(3, "value_3")

    def test(self):
        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(2, self.tree.Root.LeftChild.NodeKey)
        self.assertEqual(3, self.tree.Root.LeftChild.RightChild.NodeKey)

        self.tree.DeleteNodeByKey(2)
        self.assertEqual(4, self.tree.Root.LeftChild.Parent.NodeKey)
        self.assertEqual(3, self.tree.Root.LeftChild.NodeKey)
        self.assertIsNone(self.tree.Root.LeftChild.RightChild)
        self.assertIsNone(self.tree.Root.LeftChild.LeftChild)
        self.assertFalse(self.tree.FindNodeByKey(2).NodeHasKey)


class RemoveLeftNotLeafNodeWithChildrenTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BST(None)
        self.tree.AddKeyValue(4, "value_4")
        self.tree.AddKeyValue(2, "value_2")
        self.tree.AddKeyValue(6, "value_6")
        self.tree.AddKeyValue(1, "value_1")
        self.tree.AddKeyValue(3, "value_3")

    def test(self):
        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(2, self.tree.Root.LeftChild.NodeKey)
        self.assertEqual(1, self.tree.Root.LeftChild.LeftChild.NodeKey)
        self.assertEqual(3, self.tree.Root.LeftChild.RightChild.NodeKey)

        self.tree.DeleteNodeByKey(2)

        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(3, self.tree.Root.LeftChild.NodeKey)
        self.assertEqual(1, self.tree.Root.LeftChild.LeftChild.NodeKey)
        self.assertIsNone(self.tree.Root.LeftChild.RightChild)


class RemoveLeftLeafNodeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BST(None)
        self.tree.AddKeyValue(4, "value_4")
        self.tree.AddKeyValue(2, "value_2")
        self.tree.AddKeyValue(6, "value_6")
        self.tree.AddKeyValue(1, "value_1")
        self.tree.AddKeyValue(3, "value_3")

    def test_left(self):
        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(2, self.tree.Root.LeftChild.NodeKey)
        self.assertEqual(1, self.tree.Root.LeftChild.LeftChild.NodeKey)
        self.assertEqual(3, self.tree.Root.LeftChild.RightChild.NodeKey)

        self.tree.DeleteNodeByKey(1)

        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(2, self.tree.Root.LeftChild.NodeKey)
        self.assertIsNone(self.tree.Root.LeftChild.LeftChild)
        self.assertEqual(3, self.tree.Root.LeftChild.RightChild.NodeKey)

    def test_right(self):
        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(2, self.tree.Root.LeftChild.NodeKey)
        self.assertEqual(1, self.tree.Root.LeftChild.LeftChild.NodeKey)
        self.assertEqual(3, self.tree.Root.LeftChild.RightChild.NodeKey)

        self.tree.DeleteNodeByKey(3)

        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(2, self.tree.Root.LeftChild.NodeKey)
        self.assertIsNone(self.tree.Root.LeftChild.RightChild)
        self.assertEqual(1, self.tree.Root.LeftChild.LeftChild.NodeKey)


class RemoveRightLeafNodeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BST(None)
        self.tree.AddKeyValue(4, "value_4")
        self.tree.AddKeyValue(2, "value_2")
        self.tree.AddKeyValue(6, "value_6")
        self.tree.AddKeyValue(5, "value_5")
        self.tree.AddKeyValue(7, "value_7")

    def test_left(self):
        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(6, self.tree.Root.RightChild.NodeKey)
        self.assertEqual(5, self.tree.Root.RightChild.LeftChild.NodeKey)
        self.assertEqual(7, self.tree.Root.RightChild.RightChild.NodeKey)

        self.tree.DeleteNodeByKey(5)

        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(6, self.tree.Root.RightChild.NodeKey)
        self.assertIsNone(self.tree.Root.RightChild.LeftChild)
        self.assertEqual(7, self.tree.Root.RightChild.RightChild.NodeKey)

    def test_right(self):
        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(6, self.tree.Root.RightChild.NodeKey)
        self.assertEqual(5, self.tree.Root.RightChild.LeftChild.NodeKey)
        self.assertEqual(7, self.tree.Root.RightChild.RightChild.NodeKey)

        self.tree.DeleteNodeByKey(7)

        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(6, self.tree.Root.RightChild.NodeKey)
        self.assertIsNone(self.tree.Root.RightChild.RightChild)
        self.assertEqual(5, self.tree.Root.RightChild.LeftChild.NodeKey)


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

        self.tree.DeleteNodeByKey(7)
        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(6, self.tree.Root.RightChild.NodeKey)
        self.assertEqual(8, self.tree.Root.RightChild.RightChild.NodeKey)
        self.assertEqual(10, self.tree.Root.RightChild.RightChild.RightChild.NodeKey)
        self.assertEqual(11, self.tree.Root.RightChild.RightChild.RightChild.RightChild.NodeKey)
        self.assertEqual(9, self.tree.Root.RightChild.RightChild.RightChild.LeftChild.NodeKey)
        self.assertIsNone(self.tree.Root.RightChild.RightChild.RightChild.LeftChild.LeftChild)


class RemoveFromAdvanceTreeWithRightAddNodesTestCase(BaseBinarySearchTreeTestCase):
    def test(self):
        self.tree.AddKeyValue(12, "value_12")
        self.tree.AddKeyValue(13, "value_13")
        self.tree.AddKeyValue(11, "value_11")
        self.tree.AddKeyValue(9, "value_9")
        self.tree.AddKeyValue(10, "value_10")

        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(6, self.tree.Root.RightChild.NodeKey)
        self.assertEqual(7, self.tree.Root.RightChild.RightChild.NodeKey)
        self.assertEqual(12, self.tree.Root.RightChild.RightChild.RightChild.NodeKey)
        self.assertEqual(13, self.tree.Root.RightChild.RightChild.RightChild.RightChild.NodeKey)
        self.assertEqual(11, self.tree.Root.RightChild.RightChild.RightChild.LeftChild.NodeKey)
        self.assertEqual(9, self.tree.Root.RightChild.RightChild.RightChild.LeftChild.LeftChild.NodeKey)

        self.tree.DeleteNodeByKey(7)
        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(6, self.tree.Root.RightChild.NodeKey)
        self.assertEqual(9, self.tree.Root.RightChild.RightChild.NodeKey)
        self.assertEqual(12, self.tree.Root.RightChild.RightChild.RightChild.NodeKey)
        self.assertEqual(13, self.tree.Root.RightChild.RightChild.RightChild.RightChild.NodeKey)
        self.assertEqual(11, self.tree.Root.RightChild.RightChild.RightChild.LeftChild.NodeKey)
        self.assertEqual(10, self.tree.Root.RightChild.RightChild.RightChild.LeftChild.LeftChild.NodeKey)


class RemoveFromLargeTreeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BST(None)
        self.tree.AddKeyValue(8, "")
        self.tree.AddKeyValue(4, "")
        self.tree.AddKeyValue(12, "")
        self.tree.AddKeyValue(2, "")
        self.tree.AddKeyValue(6, "")
        self.tree.AddKeyValue(1, "")
        self.tree.AddKeyValue(5, "")
        self.tree.AddKeyValue(7, "")
        self.tree.AddKeyValue(10, "")
        self.tree.AddKeyValue(14, "")
        self.tree.AddKeyValue(11, "")
        self.tree.AddKeyValue(13, "")
        self.tree.AddKeyValue(15, "")
        self.tree.AddKeyValue(16, "")

        self.assertEqual(8, self.tree.Root.NodeKey)
        self.assertEqual(4, self.tree.Root.LeftChild.NodeKey)
        self.assertEqual(2, self.tree.Root.LeftChild.LeftChild.NodeKey)
        self.assertEqual(1, self.tree.Root.LeftChild.LeftChild.LeftChild.NodeKey)
        self.assertEqual(6, self.tree.Root.LeftChild.RightChild.NodeKey)
        self.assertEqual(7, self.tree.Root.LeftChild.RightChild.RightChild.NodeKey)
        self.assertEqual(5, self.tree.Root.LeftChild.RightChild.LeftChild.NodeKey)

        self.assertEqual(12, self.tree.Root.RightChild.NodeKey)
        self.assertEqual(10, self.tree.Root.RightChild.LeftChild.NodeKey)
        self.assertEqual(11, self.tree.Root.RightChild.LeftChild.RightChild.NodeKey)
        self.assertEqual(14, self.tree.Root.RightChild.RightChild.NodeKey)
        self.assertEqual(13, self.tree.Root.RightChild.RightChild.LeftChild.NodeKey)
        self.assertEqual(15, self.tree.Root.RightChild.RightChild.RightChild.NodeKey)
        self.assertEqual(16, self.tree.Root.RightChild.RightChild.RightChild.RightChild.NodeKey)

    def test_1(self):
        self.tree.DeleteNodeByKey(1)
        self.assertEqual(2, self.tree.Root.LeftChild.LeftChild.NodeKey)
        self.assertIsNone(self.tree.Root.LeftChild.LeftChild.LeftChild)

    def test_2(self):
        self.tree.DeleteNodeByKey(2)
        self.assertEqual(1, self.tree.Root.LeftChild.LeftChild.NodeKey)

    def test_3(self):
        self.tree.DeleteNodeByKey(4)
        self.assertEqual(5, self.tree.Root.LeftChild.NodeKey)
        self.assertEqual(2, self.tree.Root.LeftChild.LeftChild.NodeKey)
        self.assertEqual(6, self.tree.Root.LeftChild.RightChild.NodeKey)
        self.assertEqual(7, self.tree.Root.LeftChild.RightChild.RightChild.NodeKey)
        self.assertIsNone(self.tree.Root.LeftChild.RightChild.LeftChild)

    def test_4(self):
        self.tree.DeleteNodeByKey(6)
        self.assertEqual(4, self.tree.Root.LeftChild.NodeKey)
        self.assertEqual(7, self.tree.Root.LeftChild.RightChild.NodeKey)
        self.assertEqual(5, self.tree.Root.LeftChild.RightChild.LeftChild.NodeKey)

    def test_5(self):
        self.tree.DeleteNodeByKey(11)
        self.assertEqual(10, self.tree.Root.RightChild.LeftChild.NodeKey)
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.RightChild)

    def test_6(self):
        self.tree.DeleteNodeByKey(10)
        self.assertEqual(11, self.tree.Root.RightChild.LeftChild.NodeKey)

    def test_7(self):
        self.tree.DeleteNodeByKey(14)
        self.assertEqual(15, self.tree.Root.RightChild.RightChild.NodeKey)
        self.assertEqual(16, self.tree.Root.RightChild.RightChild.RightChild.NodeKey)
        self.assertEqual(13, self.tree.Root.RightChild.RightChild.LeftChild.NodeKey)


class RemoveRootTestCase(BaseBinarySearchTreeTestCase):
    def test(self):
        self.assertEqual(4, self.tree.Root.NodeKey)
        self.tree.DeleteNodeByKey(4)
        self.assertEqual(5, self.tree.Root.NodeKey)


class RemoveFromTreeWithSingleNodeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BST(None)
        self.tree.AddKeyValue(4, "value_4")

    def test(self):
        self.assertEqual(4, self.tree.Root.NodeKey)
        self.tree.DeleteNodeByKey(4)
        self.assertIsNone(self.tree.Root)


class RemoveFromTreeWithSeveralNodes(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BST(None)
        self.tree.AddKeyValue(4, "value_4")

    def test_left(self):
        self.tree.AddKeyValue(2, "value_2")

        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(2, self.tree.Root.LeftChild.NodeKey)
        self.assertEqual(4, self.tree.Root.LeftChild.Parent.NodeKey)

        self.tree.DeleteNodeByKey(2)

        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertIsNone(self.tree.Root.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild)

    def test_right(self):
        self.tree.AddKeyValue(6, "value_2")

        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(6, self.tree.Root.RightChild.NodeKey)
        self.assertEqual(4, self.tree.Root.RightChild.Parent.NodeKey)

        self.tree.DeleteNodeByKey(6)

        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertIsNone(self.tree.Root.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild)


class RemoveMultipleTimesTestCase(BaseBinarySearchTreeTestCase):
    def test(self):
        self.tree.DeleteNodeByKey(2)
        self.tree.DeleteNodeByKey(6)
        self.tree.DeleteNodeByKey(3)
        self.tree.DeleteNodeByKey(1)
        self.tree.DeleteNodeByKey(7)
        self.tree.DeleteNodeByKey(5)
        self.tree.DeleteNodeByKey(4)

        self.assertIsNone(self.tree.Root)


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


class CountWithInitNodeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BST(BSTNode(4, "value_4", None))

    def test(self):
        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(1, self.tree.Count())


class CountTreeWithSingleNodeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BST(None)
        self.tree.AddKeyValue(4, "value_4")

    def test(self):
        self.assertEqual(4, self.tree.Root.NodeKey)
        self.assertEqual(1, self.tree.Count())


if __name__ == '__main__':
    unittest.main()
