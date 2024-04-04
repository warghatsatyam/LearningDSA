from math import *
from collections import *
from sys import *
from os import *


def subset(arr):
    if len(arr) == 0:
        arr = []
        arr.append([])
        return arr
    smallerSubset = subset(arr[1:])    
    
    output = []
    for ele in smallerSubset:
        output.append(ele)
        output.append([arr[0]]+ele)
    return output    



n = input()
arr = [int(ele) for ele in input().split()]
output = subset(arr)

for elem in output:
    if elem != []:
        for num in elem:
            print(num,end = ' ')
        print()   