def push_zero_to_end_code(arr,n):
    non_zero_position = 0
    for x in range(n):
        if arr[x]!=0:
            arr[x],arr[non_zero_position] = arr[non_zero_position],arr[x]
            non_zero_position+=1
    return arr





if __name__ == '__main__':
    arr = [2,0,0,1,3,0,0]
    n = len(arr)
    output_arr = push_zero_to_end_code(arr,n)
    print(output_arr)