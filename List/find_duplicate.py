def get_duplicatet(arr):
    hashmap = {}
    for x in arr:
        a = hashmap.get(x,0)
        if a==0:
            hashmap[x]=1
        else:
            hashmap[x]+=1
    for x in hashmap.keys():
        if hashmap[x] == 2:
            return x
    return -1

if __name__ == '__main__':
    arr = [0,7,2,6,4,7,1,3,6]
    unique_ele = get_duplicatet(arr)
    print(unique_ele)