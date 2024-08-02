'''
https://leetcode.com/problems/permutations-ii/
- only diff input might contain dublicates
- but rest can't have any dublicate set
'''
#%%
from typing import List
from itertools import permutations


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return set(permutations(nums))

s= Solution()
#%%
s.permuteUnique([1, 2, 3])
# %%
# [[1,1,2], [1,2,1], [2,1,1]]
s.permuteUnique([1, 2, 1])
# %%
# my equvalet solution
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def helper(i):
            if i == len(nums) - 1:
                res.append(nums[:])
                return
            
            hash = {}
            for j in range(i, len(nums)):
                if nums[j] not in hash:
                    hash[nums[j]] = True
                    nums[i], nums[j] = nums[j], nums[i]
                    helper(i+1)
                    nums[i], nums[j] = nums[j], nums[i]
        helper(0)
        return res

