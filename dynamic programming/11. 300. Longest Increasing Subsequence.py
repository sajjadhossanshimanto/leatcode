# https://leetcode.com/problems/longest-increasing-subsequence/

#%%
from typing import List
from functools import lru_cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(start):
            max_length = 1  # The current element itself forms a subsequence of length 1
            for i in range(start + 1, len(nums)):
                if nums[i] > nums[start]:
                    max_length = max(max_length, dfs(i) + 1)
            return max_length

        return max(dfs(i) for i in range(len(nums)))


s = Solution()
# %%
s.lengthOfLIS(
    [7,7,7,7,7,7,7]
)
# %%
# ans: 4
s.lengthOfLIS(
    [0,1,0,3,2,3]
)
# %%
s.lengthOfLIS(
    [10,9,2,5,3,7,101,18]
)
# %%
s.lengthOfLIS(
    [1, 2, 3, 4, 5]
)
# %%
