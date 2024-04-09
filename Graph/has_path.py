# Write your code here
from sys import stdin

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

    def __has_path_helper(self,v1,v2,visited_nodes):
        if self.adjMatrix[v1][v2]==1:
            return True
        get_adjacent_vertex = []
        for i in range(self.nVertices):
            if self.adjMatrix[v1][i] == 1 and visited_nodes[i]== False:
                get_adjacent_vertex.append(i)

        visited_nodes[v1] = True
        has_path = False 
        for x in get_adjacent_vertex:
            ans = self.__has_path_helper(x,v2,visited_nodes)
            if ans:
                return True
        return has_path

    def has_path(self,v1,v2,V):
        if v2<self.nVertices:
            visited_nodes = [False for i in range(self.nVertices)]
            ans = self.__has_path_helper(v1,v2,visited_nodes)
            if ans == True:
                print("true")
            else:
                print("false")
        else:
            print("false")
        
# Main
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
g.has_path(v1,v2,V)