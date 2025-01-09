# https://leetcode.com/problems/target-sum/

#%%
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target = (sum(nums)-target)//2
        # print(target)

        def backtrack(start=0, presum=0):
            if presum==target:
                return 1
            if presum>target: return 0

            count = 0
            for i in range(start, len(nums)):
                count += backtrack(i+1, presum+nums[i])
            
            return count
        
        return backtrack()


s = Solution()
# %% 
# ans = 5
s.findTargetSumWays(nums = [1,1,1,1,1], target = 3)
# %%
