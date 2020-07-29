import unittest
from balanced_binary_search_tree import BalancedBST, BSTNode


class GenerateTreeFromEmptyListTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BalancedBST()

    def test(self):
        self.tree.GenerateTree([])
        self.assertIsNone(self.tree.Root)


class GenerateTreeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BalancedBST()

    def test(self):
        self.assertIsNone(self.tree.Root)
        self.tree.GenerateTree([81, 92, 55, 63, 31, 43, 84, 21, 19, 62, 37, 50, 25, 20, 75])

        self.assertEqual(50, self.tree.Root.NodeKey)
        self.assertIsNone(self.tree.Root.Parent)
        self.assertEqual(1, self.tree.Root.Level)

        self.assertEqual(25, self.tree.Root.LeftChild.NodeKey)
        self.assertEqual(50, self.tree.Root.LeftChild.Parent.NodeKey)

        self.assertEqual(75, self.tree.Root.RightChild.NodeKey)
        self.assertEqual(50, self.tree.Root.RightChild.Parent.NodeKey)

        self.assertEqual(2, self.tree.Root.LeftChild.Level)

        self.assertEqual(20, self.tree.Root.LeftChild.LeftChild.NodeKey)
        self.assertEqual(25, self.tree.Root.LeftChild.LeftChild.Parent.NodeKey)

        self.assertEqual(84, self.tree.Root.RightChild.RightChild.NodeKey)
        self.assertEqual(75, self.tree.Root.RightChild.RightChild.Parent.NodeKey)

        self.assertEqual(3, self.tree.Root.LeftChild.LeftChild.Level)
        self.assertEqual(3, self.tree.Root.RightChild.RightChild.Level)


class IsBalancedTreeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BalancedBST()
        self.tree.GenerateTree([81, 92, 55, 63, 31, 43, 84, 21, 19, 62, 37, 50, 25, 20, 75])

    def test(self):
        self.assertTrue(self.tree.IsBalanced(self.tree.Root))


class IsNotBalancedTreeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BalancedBST()
        node_50 = BSTNode(50, None)
        node_25 = BSTNode(25, node_50)
        node_75 = BSTNode(75, node_50)
        node_62 = BSTNode(62, node_75)
        node_84 = BSTNode(84, node_75)
        node_55 = BSTNode(55, node_62)

        node_50.LeftChild = node_25
        node_50.RightChild = node_75
        node_75.LeftChild = node_62
        node_75.RightChild = node_84
        node_62.LeftChild = node_55

        self.tree.Root = node_50

    def test(self):
        self.assertFalse(self.tree.IsBalanced(self.tree.Root))
