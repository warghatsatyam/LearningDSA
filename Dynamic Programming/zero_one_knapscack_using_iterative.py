
def knapsack(W,val,wt):
    n = len(val)
    dp = [[0 for j in range(W+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,W+1):

            if j < wt[i-1]:
                ans = dp[i-1][j]
            else:
                ans1 = val[i-1] + dp[i-1][j-wt[i-1]]
                ans2 = dp[i-1][j]
                ans = max(ans1,ans2)
            dp[i][j] = ans 
    return dp[n][W]

if __name__ == '__main__':
    wt = [1,2,3,4]
    val = [20,15,10,24]
    W = 5
    ans = knapsack(W,val,wt)
    print(ans)