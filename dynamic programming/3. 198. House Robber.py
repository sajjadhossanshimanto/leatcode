# https://leetcode.com/problems/house-robber/description/

#%%
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2: return max(nums)

        return max(
            nums[0] + self.rob(nums[2:]),
            self.rob(nums[1:])
        )

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
