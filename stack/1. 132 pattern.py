'''
https://leetcode.com/problems/132-pattern/description/
'''
#%%
from typing import List
from itertools import combinations

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        for i, j, k in combinations(nums, r = 3):
            if i<k<j:
                return True
        return False


s = Solution()
# %%
# ans = false
s.find132pattern([1,2,3,4])
# %%
# ans = 1
s.find132pattern([3,1,4,2])
# %%
# 1
s.find132pattern([-1,3,2,0])
# %%
