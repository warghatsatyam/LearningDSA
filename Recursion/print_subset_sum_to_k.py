def subset_sum_to_k(arr,output,k):
    if k==0:
        print_subset(output)
        return 
    if k<0:
        return
    if len(arr)>0:
        ele = arr[0]
        new_output = output+[ele]
        subset_sum_to_k(arr[1:],new_output,k-ele)
        subset_sum_to_k(arr[1:],output,k)


def print_subset(arr):
    for x in arr:
        print(x, end=' ')
    print()
    

n = int(input())
arr = input().split(' ')
arr = [int(x) for x in arr]
k = int(input())
output = []
subset_sum_to_k(arr,output,k)