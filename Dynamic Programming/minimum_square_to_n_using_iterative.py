
def minimum_square_to_n_using_iterative_code(n):
    dp  = [0 for i in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    i = 2
    while i<= n:
        j=1
        minV = float('inf')
        while j*j <=i:
            ans1 = dp[i-(j*j)]
            minV = min(ans1,minV)
            j+=1
        dp[i] = minV +1
        i+=1
    return dp[n]


if __name__ == '__main__':
    n = int(input("Enter n: "))
    minimum_number = minimum_square_to_n_using_iterative_code(n)
    print(minimum_number)