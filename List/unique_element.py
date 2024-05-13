def get_unique_element(arr):
    hashmap = {}
    for x in arr:
        a = hashmap.get(x,0)
        if a==0:
            hashmap[x]=1
        else:
            hashmap[x]+=1
    for x in hashmap.keys():
        if hashmap[x] == 1:
            return x
    return -1





if __name__ == '__main__':
    arr = [2,3,1,6,3,6,2,1,0]
    unique_ele = get_unique_element(arr)
    print(unique_ele)