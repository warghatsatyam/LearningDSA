def pattern_thirteen(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        for k in range(0,(2*n)-(2*i)):
            print(" ",end=" ")
        for l in range(i,0,-1):
            print(l,end=" ")
        print()

if __name__ == '__main__':
    n = int(input("Enter value of n: "))
    pattern_thirteen(n)