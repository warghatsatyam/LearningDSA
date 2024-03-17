def minimum_square_to_n_code(n,dp):
    if n==0:
        dp[0]=0
        return 0
    if n==1:
        dp[1]=1
        return 1
    minV = float('inf')
    i=1
    while i*i <=n:
        if dp[n-(i*i)]==-1:
            ans1 = 1 + minimum_square_to_n_code(n-(i*i),dp)
            dp[n-(i*i)]=ans1
        else:
            ans1 = dp[n-(i*i)]
        minV = min(minV,ans1)
        i+=1
    return minV

if __name__ == '__main__':
    n = int(input("Enter value of n: "))
    dp = [-1 for i in range(n+1)]
    minimum_square_n = minimum_square_to_n_code(n,dp)
    print(minimum_square_n)