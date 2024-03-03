# def get_pair_sum_to_zero_count(arr):
#     count = 0
#     n = len(arr)
#     for i in range(n):
#         ele1 = arr[i]
#         for j in range(i+1,n):
#             ele2 = arr[j]
#             if ele1+ele2 == 0:
#                 count+=1
#     return count

def get_pair_sum_to_zero_count(arr):
    count = 0
    d = {} 
    for x in  arr:
        if x in d:
            d[x] = d.get(x)+1
        else:
            d[x] = 1
    for x in d :
        if x !=0 and -(x) in d:
            count += d[x]*d[-x]
            d[x]=0
            d[-x]=0
        if x == 0 and d[x]!=1:
            val = d[x]
            count+=((val-1)*val)//2
    return count

if __name__ == '__main__':
    arr = [0,0,0,0]
    count = get_pair_sum_to_zero_count(arr)
    print(count)