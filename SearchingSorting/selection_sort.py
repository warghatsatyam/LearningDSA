def selection_sort(arr,n):
    for i in range(n):
        minimum = i
        for j in range(i+1,n):
            if arr[j]<arr[minimum]:
                minimum = j
        arr[i],arr[minimum] = arr[minimum],arr[i]
    return arr



if __name__ == '__main__':
    arr = [20,10,11,0,3,8,5]
    output_arr = selection_sort(arr,len(arr))
    print(output_arr)