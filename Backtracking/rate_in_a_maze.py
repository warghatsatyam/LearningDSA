

def print_path_helper(x,y,maze,n,solution):
    if x==n-1 and y==n-1:
        solution[x][y]=1
        print(solution)
        return
    if x<0 or y<0 or y>=n or x>=n or maze[x][y]==0 or solution[x][y] == 1:
        return
    
    solution[x][y]=1
    print_path_helper(x+1,y,maze,n,solution)
    print_path_helper(x,y+1,maze,n,solution)
    print_path_helper(x-1,y,maze,n,solution)
    print_path_helper(x,y-1,maze,n,solution)
    solution[x][y]=0
    return





def printPath(maze):
    n = len(maze)
    solution = [ [ 0 for j in range(n)] for i in range(n)]
    print_path_helper(0,0,maze,n,solution)




if __name__ == '__main__':
    maze = []
    n = int(input())
    for i in range(n):
        row = [ int(ele) for ele in input().split()]
        maze.append(row)
    printPath(maze)