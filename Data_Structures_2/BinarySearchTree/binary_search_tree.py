class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок

    def hasLeftChild(self):
        return self.LeftChild

    def hasRightChild(self):
        return self.RightChild

    def isLeftChild(self):
        return self.Parent and self.Parent.LeftChild == self

    def isRightChild(self):
        return self.Parent and self.Parent.RightChild == self

    def isRoot(self):
        return not self.Parent

    def isLeaf(self):
        return not (self.RightChild or self.LeftChild)

    def hasAnyChildren(self):
        return self.LeftChild or self.RightChild

    def hasBothChildren(self):
        return self.LeftChild and self.RightChild

    def splice(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.Parent.LeftChild = None
            else:
                self.Parent.RightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.Parent.LeftChild = self.LeftChild
                else:
                    self.Parent.RightChild = self.LeftChild
                self.LeftChild.parent = self.Parent
            else:
                if self.isLeftChild():
                    self.Parent.LeftChild = self.RightChild
                else:
                    self.Parent.RightChild = self.RightChild
                self.RightChild.parent = self.Parent


class BSTFind:  # промежуточный результат поиска
    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None

        element = self.queue[0]
        del self.queue[0]
        return element

    def size(self):
        return len(self.queue)


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
        return True

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

        if removable_node.isLeaf():
            if removable_node.isLeftChild():
                removable_node.Parent.LeftChild = None
            elif removable_node.isRightChild():
                removable_node.Parent.RightChild = None
            elif removable_node == self.Root:
                self.Root = None
        elif removable_node.hasBothChildren():
            successor = self.FinMinMax(removable_node.RightChild, False)
            successor.splice()
            removable_node.NodeKey = successor.NodeKey
            removable_node.NodeValue = successor.NodeValue
        else:
            if removable_node.hasLeftChild():
                if removable_node.isLeftChild():
                    removable_node.Parent.LeftChild = removable_node.LeftChild
                else:
                    removable_node.Parent.RightChild = removable_node.LeftChild
                removable_node.LeftChild.Parent = removable_node.Parent
            else:
                successor = self.FinMinMax(removable_node.RightChild, False)
                successor.splice()
                removable_node.NodeKey = successor.NodeKey
                removable_node.NodeValue = successor.NodeValue

        self.count -= 1
        return True

    def Count(self):
        """
        количество узлов в дереве
        :return:
        """

        return self.count

    def WideAllNodes(self):
        """
        обход в ширину
        :return:
        """
        if self.Root is None:
            return []

        queue = Queue()
        queue.enqueue(self.Root)
        nodes = []

        while queue.size() != 0:
            node = queue.dequeue()
            nodes.append(node)

            if node.hasLeftChild():
                queue.enqueue(node.LeftChild)

            if node.hasRightChild():
                queue.enqueue(node.RightChild)

        return nodes

    def DeepAllNodes(self, deep_type):
        """
        обход в глубину
        :param deep_type:
        :return:
        """

        def in_order_traversal(node):
            nodes = []
            if node is not None:
                nodes.extend(in_order_traversal(node.LeftChild))
                nodes.extend([node])
                nodes.extend(in_order_traversal(node.RightChild))

            return nodes

        def post_order_traversal(node):
            nodes = []
            if node is not None:
                nodes.extend(post_order_traversal(node.LeftChild))
                nodes.extend(post_order_traversal(node.RightChild))
                nodes.extend([node])

            return nodes

        def pre_order_traversal(node):
            nodes = []
            if node is not None:
                nodes.extend([node])
                nodes.extend(pre_order_traversal(node.LeftChild))
                nodes.extend(pre_order_traversal(node.RightChild))

            return nodes

        if self.Root is None:
            return []

        if deep_type == 0:
            return in_order_traversal(self.Root)
        elif deep_type == 1:
            return post_order_traversal(self.Root)
        elif deep_type == 2:
            return pre_order_traversal(self.Root)
