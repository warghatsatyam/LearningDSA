def lis(li,i,n,dp):
    if i==n:
        return 0,0
    
    including_max = 1
    for j in range(i+1,n):
        if li[j] >= li[i]:
            if dp[j] == -1:
                further_including_max = lis(li,j,n,dp)[0]+1
                dp[j]=further_including_max
            else:
                further_including_max = dp[j][0]
            including_max = max(including_max,further_including_max)
    if dp[i+1]==-1:
        excluding_max = lis(li,i+1,n,dp)[1]
        dp[i+1] = excluding_max
    else:
        excluding_max = dp[i+1][1]
    overall_max = max(including_max,excluding_max)
    print(dp)
    return including_max,overall_max

n = int(input())
li = [int(ele) for ele in input().split()]
dp = [-1 for i in range(n+1)]
ans = lis(li,0,n,dp)[1]
print(ans)