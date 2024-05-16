
def count_triplet_sum(arr,sum):
    count = 0
    arr.sort()
    n = len(arr)
    for i in range(n-2):
        left = i+1 
        right = n-1

        while left<right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == sum:
                count+=1
                left+=1
                right-=1
            elif current_sum<sum:
                left+=1
            else:
                right-=1
    return count


if __name__ == '__main__':
    arr = [2,-5,8,-6,0,5,10,11,-3]
    sum = 10
    count = count_triplet_sum(arr,sum)
    print(count)