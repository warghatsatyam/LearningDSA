from sys import stdin
import sys
sys.setrecursionlimit(10 ** 8)
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
    
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    
    def removeEdge(self):
        if self.containsEdge(v1, v2) is False :
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
    
    def containsEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] > 0:
            return True
        else: 
            return False
        
    def __str__(self):
        return str(self.adjMatrix)

    def __get_path_helper(self,v1,v2,visited_nodes):
        if v1 == v2:
            return [v2]
        
        get_adjacent_vertices = []
        for i in range(self.nVertices):
            if self.adjMatrix[v1][i] == 1 and visited_nodes[i] == False:
                get_adjacent_vertices.append(i)
        visited_nodes[v1] = True
        ans = []
        for x in get_adjacent_vertices:
            ans = self.__get_path_helper(x,v2,visited_nodes)
            if len(ans)>0:
                ans.append(v1)
                return ans
        return ans
            
    def get_path(self,v1,v2):
        if v2<self.nVertices:
            visited_nodes =[False for i in range(self.nVertices)]
            ans = self.__get_path_helper(v1,v2,visited_nodes)
            for x in ans:
                print(x,end=' ')      

li = stdin.readline().strip().split()
V = int(li[0])
E = int(li[1])

g = Graph(V)

for i in range(E) :
    arr = stdin.readline().strip().split()
    fv = int(arr[0])
    sv = int(arr[1])
    g.addEdge(fv, sv)

li = stdin.readline().strip().split()
v1 = int(li[0])
v2 = int(li[1])
g.get_path(v1,v2)