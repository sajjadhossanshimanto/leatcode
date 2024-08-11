'''
https://leetcode.com/problems/minimum-size-subarray-sum/description/
'''
#%%
from typing import List


inf = float('inf')
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = inf
        total = 0
        l = 0
        for r in range(len(nums)):
            total += nums[r]
            # if total > target:
            while total >target:
                total -= nums[l]
                l+=1

            if total==target:
                ans = min(ans, r-l+1)
        
        return 0 if ans==inf else ans

s = Solution()
#%%
# 0
s.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1])
# %%
# 1
s.minSubArrayLen( target = 4, nums = [1,4,4])
# %%
# 2
s.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])
# %%
