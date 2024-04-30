
def first_index_occurences(arr,index,size,x):
    if index==size-1 and arr[index] == x:
        return index 
    if index == size-1 and arr[index] != x:
        return -1 
    if arr[index] == x:
        return index
    
    return first_index_occurences(arr,index+1,size,x)


if __name__ == '__main__':
    arr = [4,5,3,3,2,6]
    x = int(input("Enter the value you want to find index of: "))
    is_present = first_index_occurences(arr,0,len(arr),x)
    print(is_present)
