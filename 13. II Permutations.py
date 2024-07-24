'''
- only diff input might contain dublicates
- but rest can't have any dublicate set
'''
#%%
from typing import List
from itertools import permutations


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(permutations(nums))# TODO: do i need to convert to list

s= Solution()
#%%
s.permute([1, 2, 3])
# %%
s.permute([1, 2, 1])
# %%
