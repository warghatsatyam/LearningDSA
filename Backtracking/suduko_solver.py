
def is_safe(val,i,j,n,board):
    for x in range(n):
        if (board[i][x] == val):
            return False
        
        if board[x][j] == val:
            return False
        
        if board[3*(i//3) + x//3][3*(j//3) + x%3] == val:
            return False
        
    return True

def solve_suduko(n,board):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                for val in range(1,10):
                    if is_safe(val,i,j,n,board):
                        board[i][j] = val 
                        is_correct = solve_suduko(n,board)
                        if is_correct:
                            return True
                        else:
                            board[i][j]=0
                return False
    return True

board = [[ int(ele) for ele in input().split() ]for i in range(9)]
ans = solve_suduko(9,board)
if ans is True:
    print('true')
else:
    print('false')