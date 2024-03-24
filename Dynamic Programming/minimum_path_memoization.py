import sys

def minimum_path(i,j,arr,dp):
    n = len(arr)
    m = len(arr[0])
    
    if i>=n or j>=m:
        return sys.maxsize
    
    if i==n-1 and j==m-1:
        dp[i][j]=arr[i][j]
        return dp[i][j]
    
    curr_cost = arr[i][j]
    
    if dp[i+1][j]==sys.maxsize:
        a = minimum_path(i+1,j,arr,dp)
        dp[i+1][j] = a
    else:
        a = dp[i+1][j]
    
    if dp[i+1][j+1]==sys.maxsize:
        b = minimum_path(i+1,j+1,arr,dp)
        dp[i+1][j+1] = b 
    else:
        b = dp[i+1][j+1]
        
    if dp[i][j+1] == sys.maxsize:
        c = minimum_path(i,j+1,arr,dp)
        dp[i][j+1] = c 
    else:
        c = dp[i][j+1]
    return curr_cost + min(a,b,c)

if __name__ == '__main__':
    arr = [[1,5,11],[8,13,12],[2,3,7]]
    dp = []
    for i in range(4):
        ele = []
        for j in range(4):
            ele.append(sys.maxsize)
        dp.append(ele)
    ans = minimum_path(0,0,arr,dp)
    print(ans)

