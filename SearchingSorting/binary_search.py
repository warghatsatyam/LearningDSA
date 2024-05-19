def binary_search_code(arr,x,i,j):
    while i<j:
        mid = (i+j)//2
        if arr[mid] == x:
            return mid
        elif arr[mid]>i:
            j=mid-1
        else:
            i=mid+1
    return -1



if __name__ == '__main__':
    arr = [3,4,5,6,7,8,9]
    x = 10
    index = binary_search_code(arr,x,0,len(arr)-1)
    print(index)
