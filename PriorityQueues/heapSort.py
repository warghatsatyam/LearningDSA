def percolateDown(arr,i,n):
    pi = i
    lci=2*pi+1
    rci = 2*pi+2
    while lci < n:
        miniIndex = pi
        if arr[miniIndex]>arr[lci]:
            miniIndex=lci 
        if rci < n and arr[miniIndex]>arr[rci]:
            miniIndex=rci
        if pi==miniIndex: 
            return
        arr[pi],arr[miniIndex]=arr[miniIndex],arr[pi]
        pi=miniIndex
        lci=2*pi+1
        rci=2*pi+2
    return
def heapsort(arr):
    n = len(arr)
    for i in range(n//2 -1, -1, -1):
        percolateDown(arr,i,n)

    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        percolateDown(arr,0,i)
    return        
 
arr = [int(ele) for ele in input().split()]
heapsort(arr)
for x in arr:
    print(x, end=' ')

