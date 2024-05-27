def firstIndexOccurence(arr,index,x):
    length = len(arr)
    if length == 1:
        if arr[0] == x:
            return index
        else:
            return -1
        
    if arr[0] == x:
        return index
    else:
        return firstIndexOccurence(arr[1:],index+1,x)
    

if __name__ == '__main__':
    arr = [1,2,3,4,2,1,4]
    ans = firstIndexOccurence(arr,0,14)
    print(ans)