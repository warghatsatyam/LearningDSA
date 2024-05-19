

def sort_0_1(arr):
    n = len(arr)
    i=0
    j=n-1
    while i<j:
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
            i=i+1
            j=j-1
        elif arr[i] == arr[j] and arr[i] == 0:
            i=i+1
        elif arr[i] == arr[j] and arr[j] == 1:
            j=j-1
        else:
            i=i+1
            j=j-1
    return arr 

arr = [1,1,0,0,1,0]
output = sort_0_1(arr)

print(output)