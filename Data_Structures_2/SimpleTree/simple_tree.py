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

    def RecursiveNodes(self, node):
        result = [node]
        if len(node.Children) > 0:
            for child in node.Children:
                result.extend(self.RecursiveNodes(child))

        return result

    def GetAllNodes(self):
        """
        ваш код выдачи всех узлов дерева в определённом порядке
        :return:
        """
        return self.RecursiveNodes(self.Root)

    def RecursiveFindNodeByVal(self, val, node):
        result = []
        if node.NodeValue == val:
            result.extend([node])

        if len(node.Children) > 0:
            for child in node.Children:
                result.extend(self.RecursiveFindNodeByVal(val, child))

        return result

    def FindNodesByValue(self, val):
        """
        ваш код поиска узлов по значению
        :param val:
        :return:
        """
        return self.RecursiveFindNodeByVal(val, self.Root)

    def MoveNode(self, OriginalNode, NewParent):
        """
        ваш код перемещения узла вместе с его поддеревом --
        в качестве дочернего для узла NewParent
        :param OriginalNode:
        :param NewParent:
        :return:
        """
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self):
        """
        количество всех узлов в дереве
        :return:
        """
        return len(self.GetAllNodes())

    def LeafCount(self):
        """
        количество листьев в дереве
        :return:
        """
        count = 0
        nodes = self.GetAllNodes()
        for node in nodes:
            if len(node.Children) == 0:
                count += 1

        return count
