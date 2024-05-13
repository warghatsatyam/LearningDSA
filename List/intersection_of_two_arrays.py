def get_intersection_of_arr(arr1,arr2):
    intersection_of_arr = []
    hashmap_of_arr1 = {}
    for x in arr1:
        if hashmap_of_arr1.get(x,0) == 0:
            hashmap_of_arr1[x] = 1 
        else:
            hashmap_of_arr1[x]+=1 
    
    for x in arr2:
        if x in hashmap_of_arr1 and hashmap_of_arr1[x]!=0:
            intersection_of_arr.append(x)
            hashmap_of_arr1[x]-=1
    return intersection_of_arr





if __name__ == '__main__':
    arr1 = [2,6,8,5,4,3,8]
    arr2 = [2,3,4,7,8,8]
    intesection_arr = get_intersection_of_arr(arr1,arr2)
    print(intesection_arr)