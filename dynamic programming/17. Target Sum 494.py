# https://leetcode.com/problems/target-sum/

#%%
from typing import List
from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target = (sum(nums)-target)/2
        if target-int(target)!=0: return 0
        # if target&1: return 0 # even if target is odd  it will work

        @lru_cache(None)
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
s.findTargetSumWays([0], 0)# not working with dp solution
# %%
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Calculate the total sum of nums
        total_sum = sum(nums)

        # Edge case: if target is out of bounds of achievable sums
        if target > total_sum or (total_sum - target) % 2 != 0:
            return 0

        # The actual sum we need to find in subset (derived from equation)
        s = (total_sum - target) // 2

        # Initialize the DP table where dp[j] is the number of ways to sum to j
        dp = [0] * (s + 1)
        dp[0] = 1  # There's one way to get sum 0, by choosing nothing

        # Update dp table for each number in nums
        for num in nums:
            for j in range(s, num - 1, -1):  # Traverse backward to avoid overwriting
                dp[j] += dp[j - num]

        return dp[s]