
def countStairs(n):
    if n == 1:
        return 1
    if n==2:
        return 2 
    if n==3:
        return 4
    return countStairs(n-1) + countStairs(n-2) + countStairs(n-3)


if __name__ == '__main__':
    n = int(input())
    output = countStairs(n)
    print(output)

    