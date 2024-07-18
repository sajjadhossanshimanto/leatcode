'''
https://leetcode.com/problems/single-number/description/
'''
#%%
from typing import List
from itertools import accumulate
from operator import xor


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in accumulate(nums, xor):
            pass
        
        return i


b=Solution()
#%% 
b.singleNumber( nums = [2,2,1])
# %%
# general
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0# identity of xor
        for i in nums:
            ans=ans^i
        return ans