import heapq
def kLargest(lst, k):
    k_largest_ele_arr = lst[0:k]
    heapq.heapify(k_largest_ele_arr)
    for ele in lst[k:]:
        min_ele = k_largest_ele_arr[0]
        if ele > min_ele:
            heapq.heapreplace(k_largest_ele_arr,ele)
    return k_largest_ele_arr

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kLargest(lst, k)
print(*ans, sep='\n')
