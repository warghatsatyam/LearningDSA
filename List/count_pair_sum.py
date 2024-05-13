
def get_count_pair_sum(arr,sum):
    count = 0 
    hashmap = {}
    for x in arr:
        if hashmap.get(x,0)==0:
            hashmap[x]=1
        else:
            hashmap[x]+=1
    for x in arr:
        diff = sum - x 
        if diff in hashmap and hashmap[diff]>0:
            count+=1
            hashmap[diff]-=1
    return count



if __name__ == '__main__':
    arr = [0,4,1,2,5,4]
    sum = 5
    count = get_count_pair_sum(arr,sum)
    print(count)