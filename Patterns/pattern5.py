def pattern_five(n):
    for i in range(1,n+1):
        for j in range(0,n-i+1):
            print("*",end="")
        print()


if __name__ == '__main__':
    n = int(input("Enter the value: "))
    pattern_five(n)
