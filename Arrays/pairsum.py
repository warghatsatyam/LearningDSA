from os import *
from sys import *
from collections import *
from math import *

def pairSum(arr, s):
    # Write your code here.
    d = {}
    for x in arr:
        a = d.get(x,0)
        if a==0:
            d[x] = 1 
        else:
            d[x] = a + 1 
    pair_sum = []
    for x in arr:
        diff = s-x 
        if diff in d and d[diff]!=0:
            if x<=diff:
                while d[diff]!=0:
                    pair_sum.append((x,diff))
                    d[diff]-=1
    pair_sum = sorted(pair_sum,key=lambda x: x[0])
    return pair_sum

