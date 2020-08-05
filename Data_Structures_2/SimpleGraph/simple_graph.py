class Vertex:
    def __init__(self, val):
        self.Value = val


class SimpleGraph:
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        """
        ваш код добавления новой вершины
        с значением value
        в свободное место массива vertex
        :param v:
        :return:
        """
        for i in range(len(self.vertex)):
            if self.vertex[i] is None:
                self.vertex[i] = Vertex(v)
                break

    def RemoveVertex(self, v):
        """
        ваш код удаления вершины со всеми её рёбрами
        :param v:
        :return:
        """
        self.vertex[v] = None
        self.m_adjacency[v] = [0] * next(self.max_vertex for _ in range(self.max_vertex))

        for i in self.m_adjacency:
            i[v] = 0

    def IsEdge(self, v1, v2):
        """
        True если есть ребро между вершинами v1 и v2
        :param v1:
        :param v2:
        :return:
        """
        return self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1

    def AddEdge(self, v1, v2):
        """
        добавление ребра между вершинами v1 и v2
        :param v1:
        :param v2:
        :return:
        """
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        """
        удаление ребра между вершинами v1 и v2
        :param v1:
        :param v2:
        :return:
        """
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
