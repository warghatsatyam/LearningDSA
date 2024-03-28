def knapsack_using_memoization(wt,v,n,W,dp):
    if W<=0:
        return 0
    if n==1 and wt[0] > W:
        return 0
    if n==1 and wt[0] <=W:
        return v[0]
    including_wt = 0
    if wt[0]<=W:
        if dp[n-1][W-wt[0]] == 0:
            dp[n-1][W-wt[0]] = v[0] + knapsack_using_memoization(wt[1:],v[1:],n-1,W-wt[0],dp)
            including_wt =dp[n-1][W-wt[0]]
        else:
            including_wt = dp[n-1][W-wt[0]]

    if dp[n-1][W] == 0:
        excluding_wt = knapsack_using_memoization(wt[1:],v[1:],n-1,W,dp)
        dp[n-1][W] = excluding_wt
    else:
        excluding_wt = dp[n-1][W]
    return max(including_wt,excluding_wt)
    
if __name__ == '__main__':
    W = 26
    v = [24,13,23,15,16]
    wt = [12,7,11,8,9]
    n = len(wt)
    dp = [[0 for i in range(W+1)] for j in range(n+1)]
    ans = knapsack_using_memoization(wt,v,n,W,dp)
    print(ans)

    