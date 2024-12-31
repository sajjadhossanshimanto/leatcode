# https://leetcode.com/problems/house-robber/description/

#%%
from typing import List
from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache
        def rob(start):
            if len(nums)-start<=2: return max(nums[start:])

            return max(
                nums[start] + rob(start+2),
                rob(start+1)
            )
        
        return rob(0)


#%%
s = Solution()
s.rob(
    [2,7,9,3,1]
)
# %%
# wa -> ans: 4 out: 3
s.rob(
    [2,1,1,2]
)
# %%
