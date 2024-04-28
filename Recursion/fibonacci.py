def fibonacci(n):
    if n<=1:
        return n
    ans = fibonacci(n-1)+fibonacci(n-2)
    return ans 


if __name__ == '__main__':
    ans = fibonacci(10)
    print(ans)