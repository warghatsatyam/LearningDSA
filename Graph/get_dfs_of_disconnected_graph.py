import queue

class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjacencyMatrix = [[0 for j in range(nVertices)] for i in range(nVertices)]


    def addEdge(self,v1,v2):
        self.adjacencyMatrix[v1][v2] = 1
        self.adjacencyMatrix[v2][v1] = 1

    def __dfs_helper(self,sv,visited_nodes):
        print(sv)
        visited_nodes[sv] = True
        for i in range(self.nVertices):
            if self.adjacencyMatrix[sv][i]==1 and visited_nodes[i]==False:
                self.__dfs_helper(i,visited_nodes)

    def dfs(self):
        visited_nodes = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited_nodes[i] is False:
                self.__dfs_helper(i,visited_nodes)

    def removeEdge(self,v1,v2):
        if self.adjacencyMatrix[v1][v2] == 0:
            return
        self.adjacencyMatrix[v1][v2] = 0
        self.adjacencyMatrix[v2][v1] = 0

    def containsEdge(self,v1,v2):
        return True if self.adjacencyMatrix[v1][v2]==1 else False
    
    def __str__(self):
        return str(self.adjacencyMatrix)
    



g = Graph(7)

g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,6)
print(g)
g.dfs()