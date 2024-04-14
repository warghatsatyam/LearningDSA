import queue
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

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
        sv = 0
        visited_nodes = [False for i in range(self.nVertices)]
        self.__dfs_helper(sv,visited_nodes)

    def __is_connected_helper(self,sv,visited_nodes):
        visited_nodes[sv] = True
        for i in range(self.nVertices):
            if self.adjacencyMatrix[sv][i] == 1 and visited_nodes[i] == False:
                self.__is_connected_helper(i,visited_nodes)

    def __get_connected_component_helper(self,sv,visited_nodes,component):
        visited_nodes[sv] = True
        for i in range(self.nVertices):
            if self.adjacencyMatrix[sv][i] == 1 and visited_nodes[i] == False:
                component.append(i)
                ans = self.__get_connected_component_helper(i,visited_nodes,component)
                return ans
        return component
    def get_connected_component(self):
        all_connected_component = []
        sv =0
        visited_nodes = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            component = []
            if visited_nodes[i] == False:
                component.append(i)
                ans = self.__get_connected_component_helper(i,visited_nodes,component)
                all_connected_component.append(ans)
        for x in all_connected_component:
            for y in x:
                print(y,end=' ')
            print()
    
    def __str__(self):
        return str(self.adjacencyMatrix)
    



li = stdin.readline().strip().split()
V = int(li[0])
E = int(li[1])

g = Graph(V)

for i in range(E) :
    arr = stdin.readline().strip().split()
    fv = int(arr[0])
    sv = int(arr[1])
    g.addEdge(fv, sv)

g.get_connected_component()