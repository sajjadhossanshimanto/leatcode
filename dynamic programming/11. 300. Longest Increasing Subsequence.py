# https://leetcode.com/problems/longest-increasing-subsequence/

#%%
from typing import List
from functools import lru_cache


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_ln = [0]
        @lru_cache
        def dfs(start):
            if start==len(nums)-1:
                return 1
            
            r=1
            for i in range(start+1, len(nums)):
                if nums[i]>nums[start]:
                    r = dfs(i)+1
                    if r>max_ln[0]: max_ln[0] = r
            return r

        for i in range(len(nums)):
            dfs(i)
        
        return max_ln[0]

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
