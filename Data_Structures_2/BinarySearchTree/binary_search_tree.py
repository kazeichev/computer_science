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
        self.count = 1 if node is not None else 0

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

        self.count += 1

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
                return node
            else:
                return find(next_node, find_max)

        return find(FromNode, FindMax)

    def DeleteNodeByKey(self, key):
        """
        удаляем узел по ключу
        :param key:
        :return: False если узел не найден
        """

        find = self.FindNodeByKey(key)

        if find.NodeHasKey is False:
            return False

        removable_node = find.Node
        removable_parent = find.Node.Parent

        to_left = True if removable_node.NodeKey < removable_parent.NodeKey else False

        if removable_node.RightChild is None and removable_node.LeftChild is not None:  # есть только левый ребенок
            removable_node.LeftChild.Parent = removable_parent

            if to_left:
                removable_parent.LeftChild = removable_node.LeftChild
            else:
                removable_parent.RightChild = removable_node.LeftChild

        elif removable_node.RightChild is not None and removable_node.RightChild.LeftChild is None:  # есть правый, у которого нет левого
            removable_node.RightChild.Parent = removable_parent
            removable_node.RightChild.LeftChild = removable_node.LeftChild

            if to_left:
                removable_parent.LeftChild = removable_node.RightChild
            else:
                removable_parent.RightChild = removable_node.RightChild

        elif removable_node.RightChild is not None and removable_node.RightChild.LeftChild is not None:  # есть правый, у которого есть левый
            replacement_node = self.FinMinMax(removable_node.RightChild, False)

            if replacement_node.RightChild is not None:
                replacement_node.Parent.LeftChild = replacement_node.RightChild
            else:
                replacement_node.Parent.LeftChild = None

            replacement_node.RightChild = removable_node.RightChild
            replacement_node.LeftChild = removable_node.LeftChild

            if to_left:
                removable_parent.LeftChild = replacement_node
            else:
                removable_parent.RightChild = replacement_node

        else:  # Лист
            if to_left:
                removable_parent.LeftChild = None
            else:
                removable_parent.RightChild = None

        self.count -= 1

    def Count(self):
        """
        количество узлов в дереве
        :return:
        """

        return self.count
