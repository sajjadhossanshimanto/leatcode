#%%
from typing import List
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))

s= Solution()
#%%
s.permute([1, 2, 3])
# %%
# %%
def permutations(nums):
    if len(nums)==1:
        return [[nums[0]]]# coping element
    
    result = []
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permutations(nums)

        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)
    
    return result    

