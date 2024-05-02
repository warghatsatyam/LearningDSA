

def pattern_fifteen(n):
    for i in range(1,n+1):
        num = 65
        for j in range(i):
            num = 65+j
            print(chr(num),end=" ")
        print()

if __name__ == '__main__':
    n = int(input("Enter value for n: "))
    pattern_fifteen(n)