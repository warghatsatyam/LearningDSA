import sys

def minimum_path_using_iteratively(arr,i,j):
    dp = [[ sys.maxsize for j in range(len(arr[0])+1)] for i in range(len(arr)+1)]
    for i in range(len(arr)-1,-1,-1):
        for j in range(len(arr[0])-1,-1,-1):
            if i==len(arr)-1 and j==len(arr[0])-1:
                dp[i][j]=arr[i][j]
            else:
                dp[i][j] = arr[i][j] + min(dp[i+1][j],dp[i+1][j+1],dp[i][j+1])
    return dp[0][0]


if __name__ == '__main__':
    arr = [[1,5,11],[8,13,12],[2,3,7]]
    ans = minimum_path_using_iteratively(arr,0,0)
    print(ans)