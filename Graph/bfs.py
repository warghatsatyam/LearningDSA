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
    



g = Graph(5)

g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(2,3)
g.addEdge(2,4)
print(g)
# g.dfs()
g.bfs()