import heapq
def kthLargest(lst, k):
    heapq._heapify_max(lst)
    for i in range(k-1):
        heapq._heappop_max(lst)
    return lst[0]




# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)