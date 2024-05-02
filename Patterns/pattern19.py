



def pattern_ninteen(n):
    num = 69
    for i in range(1,n+1):
        inner_num = num 
        for j in range(i):
            print(chr(inner_num),end=" ")
            inner_num+=1
        print()
        num = num -1


if __name__ == '__main__':
    n = int(input("Enter value of n: "))
    pattern_ninteen(n)