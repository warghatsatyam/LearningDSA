from math import *
from collections import *
from sys import *
from os import *
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # write the code  logic here !!! 
        if len(nums) == 0:
            nums = []
            nums.append([])
            return nums 
        smaller_subset = self.subsetsWithDup(nums[1:])
        output = []
        for ele in smaller_subset:
            if ele not in output:
                output.append(ele)
            new_ele = [nums[0]] + ele  
            if new_ele not in output:
                output.append(new_ele)
        return output

if __name__ == "__main__":
    n= int (input())
    nums=list(map(int, input().split()))  
    obj = Solution()
    ans = obj.subsetsWithDup(nums)
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print()