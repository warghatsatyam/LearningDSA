def minimum_square_to_n_code(n):
    if n==0:
        return 0
    if n==1:
        return 1
    minV = float('inf')
    i=1
    while i*i <=n:
        ans1 = 1 + minimum_square_to_n_code(n-(i*i))
        minV = min(minV,ans1)
        i+=1
    return minV

if __name__ == '__main__':
    n = int(input("Enter value of n: "))
    minimum_square_n = minimum_square_to_n_code(n)
    print(minimum_square_n)