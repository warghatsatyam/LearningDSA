
def power(x,n):
    if n==0:
        return 1 
    return x * power(x,n-1)


if __name__ == '__main__':
    n = int(input())
    x = int(input())
    output = power(x,n)
    print(output)
    