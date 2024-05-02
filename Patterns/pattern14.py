

def pattern_fourteen(n):
    num = 1 
    for i in range(1,n+1):
        for j in range(i):
            print(num,end=" ")
            num+=1
        print()

if __name__ == '__main__':
    n = int(input("Enter value for n: "))
    pattern_fourteen(n)