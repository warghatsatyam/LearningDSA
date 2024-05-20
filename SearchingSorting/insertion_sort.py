def insertion_sort_code(arr,n):
    for x in range(1,len(arr)):
        key = arr[x]
        j = x-1

        while j>=0 and key < arr[j]:
            arr[j+1],arr[j] = arr[j],arr[j+1]
            j=j-1
        arr[j+1] = key
    return arr




if __name__ == '__main__':
    arr = [-2,45,0,1,-3,7]
    n = len(arr)
    output_arr = insertion_sort_code(arr,n)
    print(output_arr)
    