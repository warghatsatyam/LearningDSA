import heapq
def kSmallest(lst, k):
    k_small_ele_arr=lst[0:k]
    heapq._heapify_max(k_small_ele_arr)
    for ele in lst[k:]:
        max_ele = k_small_ele_arr[0]
        if ele < max_ele:
            heapq._heapreplace_max(k_small_ele_arr,ele)
    return k_small_ele_arr


# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
ans.sort()
print(*ans, sep=' ')