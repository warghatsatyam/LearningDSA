import heapq

li = [9,2,0,5,6,3,1,10]
heapq.heapify(li)
print(li) #[0,2,1,5,6,3,9,10]


heapq.heappush(li,2)
print(li)  # [0,2,1,2,6,3,9,10,5]


heapq.heappop(li) # Removes minimum element
print(li)

heapq.heapreplace(li,8)  # it replaces the min element with the 8 and then heapify it to maintain heap property
print(li)

