class BSTNode:
    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 1  # уровень узла


class BalancedBST:
    def __init__(self):
        self.Root = None  # корень дерева

    def GenerateTree(self, a):
        """
        создаём дерево с нуля из неотсортированного массива a
        :param a:
        :return:
        """

        def binary_generate(parent, array):
            if not array:
                return None

            center = int(len(array) / 2)
            node = BSTNode(array[center], parent)

            if parent is not None:
                node.Level = parent.Level + 1

            node.LeftChild = binary_generate(node, array[:center])
            node.RightChild = binary_generate(node, array[center + 1:])

            return node

        self.Root = binary_generate(None, sorted(a))

    def IsBalanced(self, root_node):
        """
        сбалансировано ли дерево с корнем root_node
        :param root_node:
        :return:
        """
        if root_node is None:
            return True

        def is_balanced(node):
            if node is None:
                return 0

            return max(is_balanced(node.LeftChild), is_balanced(node.RightChild)) + 1

        left = is_balanced(root_node.LeftChild)
        right = is_balanced(root_node.RightChild)

        if (abs(left - right) <= 1) and self.IsBalanced(root_node.LeftChild) is True and self.IsBalanced(
                root_node.RightChild) is True:
            return True

        return False
