

def pattern_sixteen(n):
    for i in range(1,n+1):
        num = 65
        for j in range(n-i+1):
            num = 65+j
            print(chr(num),end=" ")
        print()

if __name__ == '__main__':
    n = int(input("Enter value for n: "))
    pattern_sixteen(n)