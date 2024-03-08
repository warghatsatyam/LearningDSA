def longest_subarray_sum_to_zero_code(arr):
    d = {}
    max_len = 0
    max_sub_arr = []
    index = 0
    sum=0
    for x in arr:
        sum+=x
        if sum == 0:
            curr_sub_arr = arr[sum:index+1]
            len_curr_arr = len(curr_sub_arr)
            if len_curr_arr>max_len:
                max_len = len_curr_arr
                max_sub_arr=curr_sub_arr
                print(max_sub_arr)
        if sum in d:
            curr_sub_arr = arr[d[sum]+1:index+1]
            len_curr_arr = len(curr_sub_arr)
            if len_curr_arr>max_len:
                max_sub_arr = curr_sub_arr
                max_len = len_curr_arr
                print(max_sub_arr)
        if sum not in d:
            d[sum] = index 
        print(max_sub_arr)
    index+=1
    return max_sub_arr

if __name__ == '__main__':
    arr = [6,1,5,-8,-4,2]
    response_arr = longest_subarray_sum_to_zero_code(arr)
    print(response_arr)