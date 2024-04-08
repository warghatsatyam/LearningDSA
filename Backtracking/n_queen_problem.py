def is_safe(x,y,board,n):
    i = x-1
    while i>=0:
        if board[i][y] == 1:
            return False
        i-=1
    
    i = x-1
    j = y-1

    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1

    i = x-1
    j = y+1
    while i>=0 and j<n:
        if board[i][j] == 1:
            return False
        i-=1
        j+=1

    return True

def n_queen_helper(row,n,board):
    if row == n:
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=' ')
        print()
        return
    for col in range(n):
        if is_safe(row,col,board,n) is True:
            board[row][col] = 1
            n_queen_helper(row+1,n,board)
            board[row][col] = 0
    return

def n_queen(n):
    board = [[0 for j in range(n)] for i in range(n)]
    n_queen_helper(0,n,board)



n = int(input())
n_queen(n)