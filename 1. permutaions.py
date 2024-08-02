'''
https://leetcode.com/problems/permutations/
'''
#%%
from typing import List
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))

s= Solution()
#%%
#  [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
s.permute([1, 2, 3])
# %%
s.permute([0, 1])
# %%
s.permute([1])
# %%
