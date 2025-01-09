# https://leetcode.com/problems/target-sum/

#%%
from typing import List
from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target = (sum(nums)-target)/2
        if target-int(target)!=0: return 0

        @lru_cahce(None)
        def backtrack(start=0, presum=0):
            count = 0
            if presum==target:
                count=1
                # return 1 # edge case 1: there might exists zeros ahead which needs to count
            if presum>target: return 0

            for i in range(start, len(nums)):
                count += backtrack(i+1, presum+nums[i])
            
            return count
        
        return backtrack()


s = Solution()
# %% 
# ans = 5
s.findTargetSumWays(nums = [1,1,1,1,1], target = 3)
# %%
# ans: 2
s.findTargetSumWays([1, 0], 1)
# %%
# ans: 0
'''
test case failed due to fraction chekcking
'''
s.findTargetSumWays([7,9,3,8,0,2,4,8,3,9], 0)
#%%
# ans: 2
'''as the ans is 2 it is totaly clear that they are asking for a 
    pick and nonpick solution
'''
s.findTargetSumWays([0], 0)
# %%
