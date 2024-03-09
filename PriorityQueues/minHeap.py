
def percolateUp(arr):
    childIndex = len(arr)-1
    while childIndex > 0:
        parentIndex = (childIndex-1)//2
        if arr[childIndex]<arr[parentIndex]:
            arr[childIndex],arr[parentIndex]=arr[parentIndex],arr[childIndex]
            childIndex=parentIndex
        else:
            break

def create_heap(arr):
    min_heap = []
    for x in arr:
        min_heap.append(x)
        percolateUp(min_heap)
    return min_heap

if __name__ == '__main__':
    arr = [10,5,8,1,4]
    min_heap = create_heap(arr)
    print(min_heap)

