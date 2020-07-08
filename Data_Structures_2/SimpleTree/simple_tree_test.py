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


if __name__ == '__main__':
    unittest.main()
