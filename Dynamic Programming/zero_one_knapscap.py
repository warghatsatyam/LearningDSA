def zero_one_knapscap_using_recursion(wt,v,n,W):
    if W <= 0:
        return 0 
    if n==1 and wt[0]>W:
        return 0
    if n==1 and wt[0] <=W:
        return v[0]
    if wt[0]<=W:
        including_wt = v[0] + zero_one_knapscap_using_recursion(wt[1:],v[1:],n-1,W-wt[0])
    else:
        including_wt = 0
    excluding_wt = zero_one_knapscap_using_recursion(wt[1:],v[1:],n-1,W)
    return max(including_wt,excluding_wt)

if __name__ == '__main__':
    wt = [1,2,3,4]
    v  = [20,15,10,24]
    W  = 5
    n = len(wt)
    ans = zero_one_knapscap_using_recursion(wt,v,n,W)
    print(ans)