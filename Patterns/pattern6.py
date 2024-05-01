def pattern_six(n):
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print(j,end=" ")
        print()


if __name__ == '__main__':
    n = int(input("Enter the value: "))
    pattern_six(n)
