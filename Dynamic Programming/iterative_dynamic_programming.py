
def iterative_fibonacci(n,dp):
    dp[0]=0
    dp[1]=1
    i=2
    while i<=n:
        dp[i]=dp[i-1]+dp[i-2]
        i+=1
    return dp[n]



if __name__ == '__main__':
    n=int(input())
    dp=[-1 for i in range(n+1)]
    ans = iterative_fibonacci(n,dp)
    print(ans)