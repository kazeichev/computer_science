import unittest
from simple_tree import SimpleTree, SimpleTreeNode


class BaseFullSimpleTreeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.node_root = SimpleTreeNode("root", None)
        self.node_1 = SimpleTreeNode("1", None)
        self.node_2 = SimpleTreeNode("2", None)
        self.node_3 = SimpleTreeNode("3", None)
        self.node_4 = SimpleTreeNode("4", None)
        self.node_5 = SimpleTreeNode("5", None)
        self.node_6 = SimpleTreeNode("6", None)

        self.tree = SimpleTree(self.node_root)

        self.tree.AddChild(self.node_1, self.node_3)
        self.tree.AddChild(self.node_1, self.node_4)

        self.tree.AddChild(self.node_2, self.node_5)
        self.tree.AddChild(self.node_2, self.node_6)

        self.tree.AddChild(self.node_root, self.node_1)
        self.tree.AddChild(self.node_root, self.node_2)


class AddChildToRootTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = SimpleTree(None)

    def test(self):
        node = SimpleTreeNode("root", None)

        self.assertIsNone(self.tree.Root)
        self.tree.AddChild(None, node)

        self.assertEqual(node, self.tree.Root)
        self.assertEqual("root", self.tree.Root.NodeValue)


class AddChildToNodeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.root_node = SimpleTreeNode("root", None)
        self.tree = SimpleTree(self.root_node)

    def test(self):
        node = SimpleTreeNode("1", None)

        self.assertEqual("root", self.tree.Root.NodeValue)
        self.tree.AddChild(self.root_node, node)

        self.assertEqual(node, self.tree.Root.Children[0])
        self.assertEqual(self.root_node, node.Parent)


class DeleteLeafNodeTestCase(BaseFullSimpleTreeTestCase):
    def test(self):
        self.assertIn(self.node_3, self.node_1.Children)
        self.assertIn(self.node_4, self.node_1.Children)

        self.tree.DeleteNode(self.node_3)

        self.assertNotIn(self.node_3, self.node_1.Children)
        self.assertEqual(1, len(self.node_1.Children))


class DeleteNodeWithChildrenTestCase(BaseFullSimpleTreeTestCase):
    def test(self):
        self.assertIn(self.node_1, self.node_root.Children)
        self.tree.DeleteNode(self.node_1)
        self.assertNotIn(self.node_1, self.node_root.Children)
        self.assertIn(self.node_2, self.node_root.Children)


class GelAllNodesTestCase(BaseFullSimpleTreeTestCase):
    def test(self):
        self.assertEqual(self.node_root, self.tree.Root)
        nodes = self.tree.GetAllNodes()
        test_nodes = [self.node_root, self.node_1, self.node_3, self.node_4, self.node_2, self.node_5, self.node_6]

        self.assertEqual(7, len(nodes))
        self.assertListEqual(nodes, test_nodes)


class FindNodeByValuesTestCase(BaseFullSimpleTreeTestCase):
    def test(self):
        self.assertEqual(self.node_root, self.tree.Root)
        self.assertEqual([self.node_5], self.tree.FindNodesByValue("5"))
        self.assertEqual([self.node_root], self.tree.FindNodesByValue("root"))
        self.assertEqual([], self.tree.FindNodesByValue("222"))


class MoveNodeTestCase(BaseFullSimpleTreeTestCase):
    def test(self):
        self.assertEqual(self.node_root, self.tree.Root)
        self.tree.MoveNode(self.node_3, self.node_2)
        self.assertIn(self.node_3, self.node_2.Children)
        self.assertListEqual([self.node_5, self.node_6, self.node_3], self.node_2.Children)

    def test_with_children(self):
        self.assertEqual(self.node_root, self.tree.Root)
        self.tree.MoveNode(self.node_1, self.node_2)
        self.assertIn(self.node_1, self.node_2.Children)
        self.assertIn(self.node_3, self.node_1.Children)
        self.assertIn(self.node_4, self.node_1.Children)


class CountNodesTestCase(BaseFullSimpleTreeTestCase):
    def test(self):
        self.assertEqual(self.node_root, self.tree.Root)
        self.assertEqual(7, self.tree.Count())


class LeafCountTestCase(BaseFullSimpleTreeTestCase):
    def test(self):
        self.assertEqual(self.node_root, self.tree.Root)
        self.assertEqual(4, self.tree.LeafCount())


class EvenTreesWithNotEvenTree(BaseFullSimpleTreeTestCase):
    def test(self):
        self.assertListEqual([], self.tree.EvenTrees())


class EvenTreesWithEvenTree(BaseFullSimpleTreeTestCase):
    def test(self):
        self.node_7 = SimpleTreeNode(7, None)
        self.tree.AddChild(self.node_6, self.node_7)
        self.assertListEqual([self.node_root, self.node_2, self.node_2, self.node_6], self.tree.EvenTrees())


if __name__ == '__main__':
    unittest.main()
