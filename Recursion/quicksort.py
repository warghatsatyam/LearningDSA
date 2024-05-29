
def quicksort(arr,low,high):
    if low<high:
        pivot_index = partition(arr,low,high)
        quicksort(arr,low,pivot_index-1)
        quicksort(arr,pivot_index+1,high)


def partition(arr,low,high):
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        print(j)
        if arr[j] <=pivot:
            print(arr[i],arr[j])
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
            print(arr)
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1


if __name__ == '__main__':
    arr = [3,6,8,10,1,2,1]
    quicksort(arr,0,len(arr)-1)
    print(arr) 