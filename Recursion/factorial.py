def printFact(n,ans):
    if n==0:
        print(ans)
        return
    ans = ans*n
    printFact(n-1,ans)

if __name__ == '__main__':
    printFact(5,1)