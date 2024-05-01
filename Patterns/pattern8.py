def pattern_eight(n):
    for i in range(1,n+1):
        for j in range(0,n-i):
            print(" ",end=" ")

        for k in range(0,i):
            print("*",end=" ")
        
        for l in range(1,i):
            print("*",end=" ")
        print()

if __name__ == '__main__':
    n = int(input("Enter the value: "))
    pattern_eight(n)
