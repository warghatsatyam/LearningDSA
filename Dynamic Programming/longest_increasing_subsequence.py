def lis(li,i,n):
    if i==n:
        return 0,0
    
    including_max = 1
    for j in range(i+1,n):
        if li[j] >= li[i]:
            further_including_max = lis(li,j,n)[0]+1
            including_max = max(including_max,further_including_max)
    excluding_max = lis(li,i+1,n)[1]
    overall_max = max(including_max,excluding_max)
    return including_max,overall_max

n = int(input())
li = [int(ele) for ele in input().split()]
ans = lis(li,0,n)[1]
print(ans)