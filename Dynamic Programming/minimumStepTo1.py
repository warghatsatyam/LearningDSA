
def minimumStepToOneCode(n):
    if n==1:
        return 0
    ans1 = minimumStepToOneCode(n-1)
    if n%2==0:
        ans2 = minimumStepToOneCode(n//2)
    else:
        ans2=float('inf')
    if n%3==0:
        ans3 = minimumStepToOneCode(n//3)
    else:
        ans3=float('inf')
    return 1 + min(ans1,ans2,ans3)

if __name__ == '__main__':
    n = int(input("Enter value of n: "))
    minimumNumber = minimumStepToOneCode(n)
    print(minimumNumber)