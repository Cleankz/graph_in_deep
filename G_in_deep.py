class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False

class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size# максимальное количество вершин
        self.m_adjacency = [[0] * size for _ in range(size)] # матрица смежности  0 отсутствие ребра 1 наличие
        self.vertex = [None] * size # хранит вершины

    def AddVertex(self, v): # сперва преобразуем в класс вертекс
        if not None in self.vertex:
            return False
        for i in range(len(self.vertex)):
            if self.vertex[i] is None:
                self.vertex[i] = Vertex(v)
                break
        # ваш код добавления новой вершины
        # с значением value
        # в свободное место массива vertex
        return


    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v): # получает на вход индекс
        self.vertex[v] = None  # ваш код удаления вершины со всеми её рёбрами
        for i in range(len(self.m_adjacency[v])):
            if self.m_adjacency[v][i] != 0:
                self.m_adjacency[v][i] = 0
        for j in range(len(self.m_adjacency)):
            if self.m_adjacency[j][v] == 1:
                self.m_adjacency[j][v] = 0
        # ваш код удаления вершины со всеми её рёбрами
        return


    def IsEdge(self, v1, v2):
        if self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1:
            return True
        # True если есть ребро между вершинами v1 и v2
        return False

    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
        # добавление ребра между вершинами v1 и v2
        return

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
        # удаление ребра между вершинами v1 и v2
        return

    def DepthFirstSearch(self, VFrom, VTo,result = []):
        if len(self.vertex) == 0:
            return result
        if VFrom >= len(self.vertex) or VTo >= len(self.vertex):
            return result
        if VFrom < 0 or VTo < 0:
            return result
        if VFrom == VTo and  self.IsEdge(VFrom,VTo) is True:
            node_from = self.vertex[VFrom]
            node_from.Hit = True
            result.append(node_from)
            return result
        if self.vertex[VFrom].Hit is False:
            result.append(self.vertex[VFrom])
            node_from = self.vertex[VFrom]
        else:
            node_from = result[0]

        if node_from.Hit is False:
            node_from.Hit = True

        if self.IsEdge(VFrom,VTo):
           self.vertex[VTo].Hit = True
           result.append(self.vertex[VTo])
           for i in range(len(self.vertex)):
               self.vertex[i].Hit = False
           return result
        else:
            for i in range(len(self.m_adjacency[VFrom])):
                if self.m_adjacency[VFrom][i] == 1 and self.vertex[i].Hit is False:
                    return self.DepthFirstSearch(i, VTo)
            result.pop(0)
            if len(result) == 0:
                for i in range(len(self.vertex)):
                    self.vertex[i].Hit = False
                return []
            else:
                result[0].Hit = True
                return self.DepthFirstSearch(VFrom, VTo)
        
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
# graff = SimpleGraph(5)
# graff.AddVertex(0)
# graff.AddVertex(1)
# graff.AddVertex(2)
# graff.AddVertex(3)
# graff.AddVertex(4)
# graff.AddEdge(0, 1)
# # graff.AddEdge(0, 2)
# # graff.AddEdge(0, 3)
# graff.AddEdge(1, 4)
# graff.AddEdge(1, 3)
# # graff.AddEdge(2, 3)
# graff.AddEdge(3, 4)
# print(graff.DepthFirstSearch(1, 1))
# print(graff.DepthFirstSearch(3, 0))