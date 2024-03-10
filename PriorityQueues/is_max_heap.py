import heapq

def checkMaxHeap(arr):
    n=len(arr)
    is_max = True 
    for i in range(n//2):
        pi = i
        lci = 2*pi+1
        rci = 2*pi+2
        if lci <n and arr[lci] > arr[pi]:
            is_max = False
            break 
        if rci <n and arr[rci] >  arr[pi]:
            is_max = False
            break
    return is_max 

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')