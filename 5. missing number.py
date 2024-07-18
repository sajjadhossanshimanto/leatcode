'''
https://leetcode.com/problems/missing-number/description/
'''
#%%
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums= set(nums)
        for i in range(len(nums)+1):
            if i not in nums:
                return i
#%%
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums= set(nums)
        arr = set(range(len(nums)+1))
        return list(arr.difference(nums))[0]

# set is not substractable
# set pop is slow
# list()[0] even faster