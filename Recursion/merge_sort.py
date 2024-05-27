def merge(arr1,arr2):
    output_arr = []
    i = 0
    j = 0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            output_arr.append(arr1[i])
            i+=1
        else:
            output_arr.append(arr2[j])
            j+=1
    
    while i < len(arr1):
        output_arr.append(arr1[i])
        i+=1

    while j < len(arr2):
        output_arr.append(arr2[j])
        j+=1
    return output_arr


def merge_sort(arr):
    if len(arr) == 1:
        return [arr[0]]
    l = 0
    r = len(arr)
    m = (l+r)//2
    left_arr = arr[0:m]
    right_arr = arr[m:]
    left_sorted_arr = merge_sort(left_arr)
    right_sorted_arr = merge_sort(right_arr)
    return merge(left_sorted_arr,right_sorted_arr)

if __name__ == '__main__':
    arr = [2,3,4,0,1,6]
    output = merge_sort(arr)
    print(output)