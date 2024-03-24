import sys

def minimum_path_using_iteratively_using_top_down_approach(arr,i,j):
    dp = [[ sys.maxsize for j in range(len(arr[0])+1)] for i in range(len(arr)+1)]
    n = len(arr)
    m = len(arr[0])
    for i in range(1,len(arr)+1):
        for j in range(1,len(arr[0])+1):
            if i==1 and j==1:
                dp[i][j]=arr[0][0]
            else:
                dp[i][j] = arr[i-1][j-1] + min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
    return dp[n][m]


if __name__ == '__main__':
    arr = [[1,5,11],[8,13,12],[2,3,7]]
    ans = minimum_path_using_iteratively_using_top_down_approach(arr,0,0)
    print(ans)