

def pattern_seventeen(n):
    num = 65
    for i in range(1,n+1):
        for j in range(i):
            print(chr(num),end=" ")
        num+=1
        print()

if __name__ == '__main__':
    n = int(input("Enter value for n: "))
    pattern_seventeen(n)