
def pattern_twelve(n):
    start = 1
    for i in range(1,n+1):
        if i%2==0:
            start = 1
        else:
            start = 0

        for j in range(0,i):
            start = 1 - start
            print(start,end=" ")
        print()



if __name__ == '__main__':
    n = int(input("What is value of n: "))
    pattern_twelve(n)
    

