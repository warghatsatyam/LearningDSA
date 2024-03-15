def minimumStepToOneCode(n, dp):
    if n==0:
        return -1
    if n == 1:
        dp[n] = 0
        return 0
    if dp[n] == -1:
        ans1 = minimumStepToOneCode(n - 1, dp)
        dp[n] = ans1
    else:
        ans1 = dp[n]
    if n % 2 == 0:
        if dp[n // 2] == -1:
            ans2 = minimumStepToOneCode(n // 2, dp)
            dp[n // 2] = ans2
        else:
            ans2 = dp[n // 2]
    else:
        ans2 = float('inf')
    if n % 3 == 0:
        if dp[n // 3] == -1:
            ans3 = minimumStepToOneCode(n // 3, dp)
            dp[n // 3] = ans3
        else:
            ans3 = dp[n // 3]
    else:
        ans3 = float('inf')
    return 1 + min(ans1, ans2, ans3)

if __name__ == '__main__':
    n = int(input("Enter value of n: "))
    dp = [-1 for _ in range(n + 1)]
    minimumNumber = minimumStepToOneCode(n, dp)
    print(minimumNumber)
