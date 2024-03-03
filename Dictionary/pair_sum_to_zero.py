def get_pair_sum_to_zero_count(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        ele1 = arr[i]
        for j in range(i+1,n):
            ele2 = arr[j]
            if ele1+ele2 == 0:
                count+=1
    return count


if __name__ == '__main__':
    arr = [2,0,1,-2,4]
    count = get_pair_sum_to_zero_count(arr)
    print(count)