class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:
    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        """
        ваш код добавления нового дочернего узла существующему ParentNode
        :param ParentNode:
        :param NewChild:
        :return:
        """

        if ParentNode is None:
            self.Root = NewChild
            return

        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete):
        """
        ваш код удаления существующего узла NodeToDelete
        :param NodeToDelete:
        :return:
        """
        if self.Root is None:
            return

        parent = NodeToDelete.Parent
        parent.Children.remove(NodeToDelete)

    def IterateNodes(self, children):
        pass

    def GetAllNodes(self):
        """
        ваш код выдачи всех узлов дерева в определённом порядке
        :return:
        """
        # return [self.Root] + self.IterateNodes(self.Root.Children)

    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        return []

    def MoveNode(self, OriginalNode, NewParent):
        # ваш код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent
        pass

    def Count(self):
        # количество всех узлов в дереве
        return 0

    def LeafCount(self):
        # количество листьев в дереве
        return 0
