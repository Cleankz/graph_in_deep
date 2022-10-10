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

    def DFirstSearch(self,VFrom, VTo,result):
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

        edges = 0
        for i in range(len(self.m_adjacency[VFrom])):
            if self.m_adjacency[VFrom][i] == 1 and self.vertex[i].Hit is False:
                edges += 1
        if edges == 0:
            result.pop(len(result)-1)
            if len(result) >= 1:
                node_from = result[len(result)-1]
            if len(result) == 0:
                return result
            for i in range(len(self.vertex)):
                if self.vertex[i] == node_from:
                    VFrom = i
        if self.IsEdge(VFrom,VTo) is False:
            for i in range(len(self.m_adjacency[VFrom])):
                if self.m_adjacency[VFrom][i] == 1 and self.vertex[i].Hit is False:
                    return self.DFirstSearch(i, VTo,result)
            result.pop(0)
            if len(result) == 0:
                for i in range(len(self.vertex)):
                    self.vertex[i].Hit = False
                return []
            else:
                result[0].Hit = True
                for i in range(len(self.vertex)):
                    if self.vertex[i] == result[0]:
                        VFrom = i
                return self.DFirstSearch(VFrom,VTo,result)
        if self.IsEdge(VFrom,VTo):
           self.vertex[VTo].Hit = True
           result.append(self.vertex[VTo])
           for i in range(len(self.vertex)):
               self.vertex[i].Hit = False
           return result
    def DepthFirstSearch(self,VFrom, VTo):
        rezult = self.DFirstSearch(VFrom, VTo,[])
        return rezult
# graff = SimpleGraph(5)
# graff.AddVertex(0)
# graff.AddVertex(1)
# graff.AddVertex(2)
# graff.AddVertex(3)
# graff.AddVertex(4)
# graff.AddEdge(4, 3)
# graff.AddEdge(2, 3)
# graff.AddEdge(4, 3)
# graff.AddEdge(4, 1)
# graff.AddEdge(0, 2)
# print(graff.DepthFirstSearch(4, 0))
# print(graff.DepthFirstSearch(3, 4))
# print(graff.DepthFirstSearch(3, 4))

# graff = SimpleGraph(5)
# graff.AddVertex(0)
# graff.AddVertex(1)
# graff.AddVertex(2)
# graff.AddVertex(3)
# graff.AddVertex(4)
# graff.AddEdge(0, 1)
# # graff.AddEdge(0, 2)
# graff.AddEdge(0, 3)
# graff.AddEdge(1, 0)
# graff.AddEdge(1, 3)
# graff.AddEdge(1, 4)
# # graff.AddEdge(2, 0)
# # graff.AddEdge(2, 4)
# graff.AddEdge(3, 0)
# graff.AddEdge(3, 1)
# # graff.AddEdge(3, 2)
# graff.AddEdge(3, 3)
# graff.AddEdge(3, 4)
# graff.AddEdge(4, 1)
# graff.AddEdge(4, 3)
# print(graff.DepthFirstSearch(0, 2))
# print(graff.DepthFirstSearch(3, 0))




        # a = 0
        # b = 0
        # for j in range(len(self.vertex)):
        #     if j != len(self.vertex)-1:
        #         if self.vertex[j] == inp_array[j]:
        #             a = j
        #         if self.vertex[j] == inp_array[j+1]:
        #             b = j
        # if i != len(inp_array)-1:
        #     if self.IsEdge(a,b) is False:
        #         inp_array.pop(i)
        #         i = 0
        #         return self.clear_way(inp_array,i)
        # else:
        #     return inp_array