

def interative_minimum_step_to_one_using_memoization_code(n):
    dp = [0 for i in range(n+1)]
    dp[0]=-1
    dp[1]=0
    dp[2]=1
    dp[3]=1
    i=4
    
    while i<=n:
        ans1 = dp[i-1]
        if i%2==0:
            ans2 = dp[i//2]
        else:
            ans2 = float('inf')
        if i%3==0:
            ans3 = dp[i//3]
        else:
            ans3 = float('inf')
        dp[i] = 1+min(ans1,ans2,ans3)
        i+=1
    return dp[n]



if __name__ == '__main__':
    n = int(input("Enter the value of n: "))
    minimum_step = interative_minimum_step_to_one_using_memoization_code(n)
    print(minimum_step)