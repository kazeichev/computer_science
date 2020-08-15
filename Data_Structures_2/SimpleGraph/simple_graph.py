class Vertex:
    def __init__(self, val):
        self.Value = val
        self.Hit = False


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

    def GetVertexNeighborIndexes(self, v):
        indexes = []

        for i in range(0, self.max_vertex):
            if self.m_adjacency[v][i] == 1:
                indexes.append(i)

        return indexes

    # Поиск в глубину
    def DepthFirstSearch(self, VFrom, VTo):
        """
        узлы задаются позициями в списке vertex
        возвращается список узлов -- путь из VFrom в VTo
        или [] если пути нету
        :param VFrom:
        :param VTo:
        :return:
        """

        for vertex in self.vertex:
            vertex.Hit = False

        def search(stack, current_vertex_index, searchable_vertex_index):
            current = self.vertex[current_vertex_index]
            current.Hit = True
            stack.push(current)

            if self.IsEdge(current_vertex_index, searchable_vertex_index):
                searchable = self.vertex[searchable_vertex_index]
                stack.push(searchable)
                return stack

            for i in self.GetVertexNeighborIndexes(current_vertex_index):
                if self.vertex[i].Hit is not True:
                    return search(stack, i, searchable_vertex_index)

            stack.pop()
            if stack.size() == 0:
                return stack

            return search(stack, self.vertex.index(stack.pop()), searchable_vertex_index)

        return search(Stack(), VFrom, VTo).get_raw_data()

    # Поиск в ширину
    def BreadthFirstSearch(self, VFrom, VTo):
        for vertex in self.vertex:
            vertex.Hit = False

        current_vertex = self.vertex[VFrom]
        searchable_vertex = self.vertex[VTo]

        queue = Queue()
        queue.enqueue(current_vertex)
        came_from = {current_vertex: None}

        while queue.size() > 0:
            current = queue.dequeue()

            if current == searchable_vertex:
                path = [current]
                while current != current_vertex:
                    current = came_from[current]
                    path.append(current)

                path.reverse()
                return path

            for vertex_id in self.GetVertexNeighborIndexes(self.vertex.index(current)):
                next_vertex = self.vertex[vertex_id]
                if next_vertex not in came_from:
                    queue.enqueue(next_vertex)
                    came_from[next_vertex] = current

        return []


class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() == 0:
            return None

        last_element = self.stack[self.size() - 1]
        self.stack = self.stack[:-1]
        return last_element

    def push(self, value):
        self.stack.append(value)

    def get_raw_data(self):
        return self.stack


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
