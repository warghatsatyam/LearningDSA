

def pattern_twenty(n):
    for i in range(1,n+1):
        for j in range(n-i+1):
            print("*",end=" ")
        for k in range(i-1):
            print(" ",end=" ")
        for l in range(i-1):
            print(" ",end=" ")
        for m in range(n-i+1):
            print("*",end=" ")
        print()
    for i in range(1,n+1):
        for j in range(i):
            print("*",end=" ")
        for k in range(n-i):
            print(" ",end=" ")
        for l in range(n-i):
            print(" ",end=" ")
        for m in range(i):
            print("*",end=" ")
        print()

if __name__ == '__main__':
    n = int(input("Enter value of n: "))
    pattern_twenty(n)