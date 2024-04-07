import sys
sys.setrecursionlimit(10 ** 8)

def subsetsSumKHelper(arr, startIndex, k) :
    if startIndex == len(arr) :
        if k == 0 :
            return [list()]
        else :
            return list()
        
    smallOutput1 = subsetsSumKHelper(arr, startIndex + 1, k) 
    smallOutput2 = subsetsSumKHelper(arr, startIndex + 1, k - arr[startIndex]) 
    print("small output 1",smallOutput1)
    print("small output 2", smallOutput2)
    output = (len(smallOutput1) + len(smallOutput2)) * [0]

    index = 0
    for i in range(len(smallOutput1)) :
        output[index] = smallOutput1[i]
        index += 1
    for i in range(len(smallOutput2)) :
        output[index] = (len(smallOutput2[i]) + 1) * [0]
        output[index][0]= arr[startIndex]
        
        for j in range(len(smallOutput2[i])) :
            output[index][j+1] = smallOutput2[i][j]
        index += 1
    print("Output",output)
    return output
        
def subsetsSumK(arr, k) :
    return subsetsSumKHelper(arr, 0, k)


k = 3
arr = [1,2,3]

print(subsetsSumK(arr,k))

# #taking input
# def takeInput() :
#     n = int(input().strip())

#     if n == 0 :
#         return list(), 0

#     arr = [int(element) for element in list(input().strip().split(" "))]
#     return arr, n


# #printing the list of lists
# def printListOfList(liOfLi) :
#     for li in liOfLi :
#         for elem in li :
#             print(elem, end = " ")
#         print()

# #main
# arr, n = takeInput()

# if n != 0 :
#     k = int(input().strip())
#     liOfLi = subsetsSumK(arr, k)

#     printListOfList(liOfLi)

