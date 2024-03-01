def get_pair_sum_to_zero_count(arr):
    d = {}
    for ele in arr:
        if ele not in d:
            d[ele]=1
        else:
            d[ele] = 1+ d.get(ele,0)
    count = 0
    for ele in d:
        if -(ele) in d and d[-ele]!=0:
            count+=1
            d[ele]=0
    return count


arr = [0,0,0,0,0]
count_pair = get_pair_sum_to_zero_count(arr)
print(count_pair)
