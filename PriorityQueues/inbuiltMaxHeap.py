import heapq

li = [1,2,3,7,9,4,0,5,8]

heapq._heapify_max(li)
print(li) # [9,8,4,7,2,3,0,5,1]

print(heapq._heappop_max(li))
print(li) #[8,7,4,5,2,3,0,1]


heapq._heapreplace_max(li,0)
print(li)

# Now to add new element

# _siftdown_max() function takes 3 input arr, end_position till we need to go 0(parent/root) and starting_pos len(arr)-1

li.append(6)
heapq._siftdown_max(li,0,len(li)-1)

print(li)

