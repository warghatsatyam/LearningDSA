def pattern_eleven(n):
    for i in range(1,2*n):
        stars = i
        if i>n:
            stars = 2*n-i
        for j in range(stars):
            print("*",end=" ")
        print()


if __name__ == '__main__':
    n = int(input("Enter value: "))
    pattern_eleven(n)
