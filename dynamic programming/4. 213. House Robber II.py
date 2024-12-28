# https://leetcode.com/problems/house-robber-ii/description/

#%%
from typing import List
from functools import lru_cache
from itertools import islice


class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache
        def rob(start, end=len(nums)):
            if end-start<=2: return max(nums[start:end])

            return max(
                nums[start] + rob(start+2, end),
                rob(start+1, end+1 if end<len(nums) else len(nums))
            )
        
        return max(rob(0, len(nums)-1), rob(1, len(nums)))


#%%
s = Solution()
s.rob(
    [2,3,2]
)
# %%
# wa -> ans: 4 out: 3
s.rob(
    [1,2,3,1]
)
# %%
