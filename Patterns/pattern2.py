
def pattern_two(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print()


if __name__ == '__main__':
    n = int(input("Enter the value: "))
    pattern_two(n)



