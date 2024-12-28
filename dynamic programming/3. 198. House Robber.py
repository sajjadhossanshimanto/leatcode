# https://leetcode.com/problems/house-robber/description/

#%%
from itertools import islice

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(
            sum(islice(nums, 0, len(nums), 2)),
            sum(islice(nums, 1, len(nums), 2))
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