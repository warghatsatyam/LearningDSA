def bubble_sort_code(arr,n):
    for i in range(n):
        swapped = False
        for j in range(0,n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    return arr





if __name__ == '__main__':
    arr = [-2,45,0,11,-9,5,3,1]
    n = len(arr)
    output_arr = bubble_sort_code(arr,n)
    print(output_arr)