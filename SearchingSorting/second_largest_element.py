def secondLargestElement(arr, n):
    largest=arr[0]
    secondlargest = -1
    for i in range(1,len(arr)):
        if arr[i]>largest:
            secondlargest = largest
            largest = arr[i]
        elif arr[i]>secondlargest:
            secondlargest=arr[i]
    return secondlargest



arr = [4,3,10,9,2]
ans = secondLargestElement(arr,4)
print(ans)