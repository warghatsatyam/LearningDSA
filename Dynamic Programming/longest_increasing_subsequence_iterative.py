
def lis(li):
    n = len(li)
    dp = [[0 for j in range(2)] for i in range(n+1)]
    for i in range(n-1,-1,-1):
        including_max = 1
        for j in range(i+1,n):
            if li[j] > li[i]:
                including_max = max(including_max,1+dp[j][0])
        dp[i][0] = including_max    
        excluding_max = dp[i+1][1]
        overall_max = max(excluding_max,including_max)
        dp[i][1] = overall_max
    return dp[0][1]


if __name__ == '__main__':
    li = [6,3,0,2,7,9]
    ans = lis(li)
    print(ans)