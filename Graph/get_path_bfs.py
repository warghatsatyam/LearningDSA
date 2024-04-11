import queue
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
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
        
    def __get_bfs_path_helper(self,v1,v2,visited,parent_dict,vertex_queue):
        if vertex_queue.empty():
            return
        ele  = vertex_queue.get()
        if ele == v2:
            vertex_queue.put(ele)
            return
        adjacent_element = []
        for i in range(self.nVertices):
            if self.adjMatrix[ele][i] == 1 and visited[i] == False:
                adjacent_element.append(i)
        visited[ele] = True
        for x in adjacent_element:
            if x == v2:
                vertex_queue.put(x)
                parent_dict[x] = ele
                return
            vertex_queue.put(x)
            parent_dict[x] = ele
        self.__get_bfs_path_helper(v1,v2,visited,parent_dict,vertex_queue)
        return
    
    def getPathBFS(self, v1,v2):
        visited = [False for i in range(self.nVertices)]
        parent_dict = {}
        vertex_queue = queue.Queue()
        vertex_queue.put(v1)
        self.__get_bfs_path_helper(v1,v2,visited,parent_dict,vertex_queue)
        path = []
        if v2 in parent_dict:
            current_vertex = v2
            while parent_dict[current_vertex] != v1:
                path.append(current_vertex)
                current_vertex = parent_dict[current_vertex]
            path += [current_vertex, v1]
        return path
        
        # write your code logic here !!!!!!!!
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

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
sv = int(li[0])
ev = int(li[1])

li = g.getPathBFS(sv, ev)

if len(li) != 0 :
	for element in li :
		print(element, end = ' ')