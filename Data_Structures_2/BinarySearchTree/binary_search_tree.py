class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска
    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:
    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def FindNodeByKey(self, key):
        """
        ищем в дереве узел и сопутствующую информацию по ключу
        возвращает BSTFind
        :param key: str
        :return: BSTFind
        """

        def search(node):
            find = BSTFind()

            if node is None:
                return find

            if node.NodeKey == key:
                find.Node = node
                find.NodeHasKey = True
                return find

            if key < node.NodeKey:
                next_node = node.LeftChild
            else:
                next_node = node.RightChild

            if next_node is None:
                find.Node = node
                find.ToLeft = True if key < node.NodeKey else False
                return find
            else:
                return search(next_node)

        return search(self.Root)

    def AddKeyValue(self, key, val):
        """
        добавляем ключ-значение в дерево
        :param key:
        :param val:
        :return: False если ключ уже есть
        """
        placement = self.FindNodeByKey(key)  # BTSFind
        node = BSTNode(key, val, placement.Node)

        if placement.NodeHasKey is True:
            return False

        if placement.Node is None:
            self.Root = node
        elif placement.ToLeft:
            placement.Node.LeftChild = node
        else:
            placement.Node.RightChild = node

    def FinMinMax(self, FromNode, FindMax):
        """
        ищем максимальное/минимальное (узел) в поддереве
        :param FromNode:
        :param FindMax:
        :return:
        """

        def find(node, find_max):
            if node is None:
                return None

            if find_max:
                next_node = node.RightChild
            else:
                next_node = node.LeftChild

            if next_node is None:
                return node.NodeKey
            else:
                return find_max(next_node, find_max)

        return find(FromNode, FindMax)

    def DeleteNodeByKey(self, key):
        """
        удаляем узел по ключу
        :param key:
        :return: False если узел не найден
        """

        find = self.FindNodeByKey(key)
        removable_node = find.Node

        if find.NodeHasKey is False:
            return False

        if removable_node.RightChild.LeftChild is None:
            replacement = removable_node.RightChild
        else:
            replacement = self.FinMinMax(removable_node.RightChild, False)

        replacement.RightChild = removable_node.RightChild
        replacement.LeftChild = removable_node.LeftChild
        replacement.Parent = removable_node.Parent

        if removable_node.Parent.NodeKey < removable_node.NodeKey:
            removable_node.Parent.RightChild = replacement
        else:
            removable_node.Parent.LeftChild = replacement

    def Count(self):
        """
        количество узлов в дереве
        :return:
        """
        def iterator(node, acc):
            if node is None:
                return acc

            acc += 1
            iterator(node.LeftChild, acc)
            iterator(node.RightChild, acc)

        return iterator(self.Root, 0)
