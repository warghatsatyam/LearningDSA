




def fib(n,dp):
    if n==0 or n==1:
        return n 
    
    if dp[n-1]==-1:
        ans1 = fib(n-1, dp)
        dp[n-1] = ans1
    else:
        dp[n-1] = ans1
    if dp[n-2] == -1:
        ans2 = fib(n-2, dp)
        dp[n-2] = ans2 
    else:
        ans2 = dp[n-2]
    return ans1+ans2



if __name__ == '__main__':
    n=int(input())
    dp=[-1 for i in range(n+1)]
    ans = fib(n,dp)
    print(ans)