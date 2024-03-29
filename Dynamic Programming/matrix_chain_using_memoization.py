

def mcm(p,i,j,dp):
    if i==j:
        return 0
    min_value = float('inf')
    for k in range(i,j):
        if dp[i][k] == -1:
            ans1 = mcm(p,i,k,dp)
            dp[i][k] = ans1
        else:
            ans1 = dp[i][k]
        
        if dp[k+1][j] == -1:
            ans2 = mcm(p,k+1,j,dp)
            dp[k+1][j] = ans2
        else:
            ans2 = dp[k+1][j]
        multiplication_cost = p[i-1]*p[k]*p[j] 
        curr_val = ans1+ans2+multiplication_cost

        min_value = min(min_value,curr_val)
    return min_value


p = [2,3,4,5,6]
n = len(p)-1
dp = [[-1 for i in range(n+1)] for j in range(n+1)]
ans = mcm(p,1,n,dp)
print(ans)
