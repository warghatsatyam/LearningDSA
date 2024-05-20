def merge_two_sorted_array(arr1,arr2):
    arr3 = []
    i = 0
    j = 0

    while i<len(arr1):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i = i+1
        else:
            arr3.append(arr2[j])
            j = j+1
        if i == len(arr1):
            arr3.extend(arr2[j:])
            break
        if j == len(arr2):
            arr3.extend(arr1[i:])
            break
    return arr3



if __name__ == '__main__':
    arr1 = [10,100,500]
    arr2 = [4,7,9]
    output_arr = merge_two_sorted_array(arr1,arr2)
    print(output_arr)