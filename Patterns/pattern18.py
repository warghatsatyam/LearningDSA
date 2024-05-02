

def pattern_eighteen(n):
    for i in range(1,n+1):
        num = 65
        for j in range(n-i):
            print(" ",end=" ")
        for k in range(i):
            print(chr(num),end=" ")
            num = num+1
        num = num-1
        for l in range(i-1):
            num = num-1
            print(chr(num),end=" ")
        print()

if __name__ == '__main__':
    n = int(input("Enter value of n: "))
    pattern_eighteen(n)