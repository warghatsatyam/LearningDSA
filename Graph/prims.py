import queue
import sys
class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjacencyMatrix = [[0 for j in range(nVertices)] for i in range(nVertices)]


    def addEdge(self,v1,v2,wt):
        self.adjacencyMatrix[v1][v2] = wt
        self.adjacencyMatrix[v2][v1] = wt

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

    def __bfs_helper(self,visited_nodes,queue):
        if queue.empty():
            return
        ele = queue.get()
        print(ele,end=" ")
        visited_nodes[ele] = True
        for i in range(self.nVertices):
            if self.adjacencyMatrix[ele][i] == 1 and visited_nodes[i] == False:
                queue.put(i)
                visited_nodes[i] = True 
        self.__bfs_helper(visited_nodes,queue)        

    def bfs(self):
        sv = 0
        vertex_queue = queue.Queue()
        vertex_queue.put(sv)
        visited_nodes = [False for i in range(self.nVertices)]
        self.__bfs_helper(visited_nodes,vertex_queue)
    

    def removeEdge(self,v1,v2):
        if self.adjacencyMatrix[v1][v2] == 0:
            return
        self.adjacencyMatrix[v1][v2] = 0
        self.adjacencyMatrix[v2][v1] = 0

    def containsEdge(self,v1,v2):
        return True if self.adjacencyMatrix[v1][v2]==1 else False
    
    def __str__(self):
        return str(self.adjacencyMatrix)
    
    def get_minVertex(self,visited,weight):
        min_vertex = -1
        for i in range(self.nVertices):
            if (visited[i]== False and (min_vertex == -1 or weight[min_vertex] > weight[i])):
                min_vertex = i
        return min_vertex

    def prims(self):
        visited = [False for i in range(self.nVertices)]
        parent  = [-1 for i in range(self.nVertices)]
        weight  = [sys.maxsize for i in range(self.nVertices)]
        
        for i in range(self.nVertices - 1):
            min_vertex = self.get_minVertex(visited,weight)
            visited[min_vertex] = True

            for j in range(self.nVertices):
                if self.adjacencyMatrix[min_vertex][j] > 0 and visited[j] == False:
                    if (weight[j] > self.adjacencyMatrix[min_vertex][j]):
                        weight[j] = self.adjacencyMatrix[min_vertex][j]
                        parent[j] = min_vertex

        for i in range(1,self.nVertices):
            if i < parent[i]:
                print(str(i)+ " " + str(parent[i]) + " " + str(weight[i]))
            else:
                print(str(parent[i]) + " " + str(i) + " " + str(weight[i]))

li = [int(ele) for ele in input().split()]
n = li[0]
E =  li[1]

g = Graph(n)

for i in range(E):
    curr_ele = [int(ele) for ele in input().split()]    
    g.addEdge(curr_ele[0],curr_ele[1],curr_ele[2])

g.prims()
