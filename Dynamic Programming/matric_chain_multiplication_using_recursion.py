

def mcm(p,i,j):
    if i==j:
        return 0
    min_value = float('inf')
    for k in range(i,j):
        ans1 = mcm(p,i,k)
        ans2 = mcm(p,k+1,j)
        multiplication_cost = p[i-1]*p[k]*p[j] 
        curr_val = ans1+ans2+multiplication_cost

        min_value = min(min_value,curr_val)
    return min_value


p = [2,3,4,5,6]
n = len(p)-1

ans = mcm(p,1,n)
print(ans)
