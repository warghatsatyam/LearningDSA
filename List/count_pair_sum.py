
def pairSum(arr,n,sum) :
    count = 0
    hashmap = {}
    for x in arr:
        if hashmap.get(x,0)==0:
            hashmap[x]=1
        else:
            hashmap[x]+=1
    
    for x in arr:
        if hashmap[x]!=0:
            compl = sum-x
            if compl in hashmap and hashmap[compl]!=0:
                count+=hashmap[x]*hashmap[compl]
                hashmap[x]=0
                hashmap[compl]=0
    return count



if __name__ == '__main__':
    arr = [0,4,1,2,5,4]
    sum = 5
    count = get_count_pair_sum(arr,sum)
    print(count)
