

def isSorted(arr,i,size):
    if size==0 or size==1:
        return True
    if arr[i]>arr[i+1]:
        return False
    return isSorted(arr,i+1,size-1)


if __name__ == '__main__':
    arr = [0,1,2,3,4]
    i=0
    size = len(arr)
    ans = isSorted(arr,i,size)
    if ans:
        print("Sorted")
    else:
        print("Not Sorted")