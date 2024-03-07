


def pair_with_difference_k(arr,k):
    d = {}
    for ele in arr:
        if ele in d:
            d[ele] = d.get(ele)+1
        else:
            d[ele] = 1
    count=0
    for x in d:
        other_pair = abs(x-k)
        if len(d)==1 and d[arr[0]]>1:
            print("In Here")
            n = d[arr[0]]
            count = ((n-1)*n)//2
            return count
        elif len(d)==1 and d[arr[0]]==1:
            print("In here 2")
            return 0
        elif other_pair in d and d[other_pair]!=0 and (x-other_pair) == k:
            count+=d[other_pair]*d[x]
            d[other_pair]-=1
            d[x]-=1
    return count


if __name__ == "__main__":
    arr = [5,1,2,4,2,2]
    count = pair_with_difference_k(arr,k=0)
    print(count)