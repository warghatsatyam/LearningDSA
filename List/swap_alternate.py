def swap_alternate(arr):
    for i in range(0,len(arr),2):
        if i!=len(arr)-1:
            next_index = i+1
            arr[i],arr[next_index] = arr[next_index],arr[i]


if __name__ == '__main__':
    arr = [9,3,6,12,4,32,5]
    swap_alternate(arr)
    print(arr)

