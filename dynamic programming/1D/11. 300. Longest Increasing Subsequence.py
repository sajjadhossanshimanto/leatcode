# https://leetcode.com/problems/longest-increasing-subsequence/

#%%
from typing import List
from functools import lru_cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1]*len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1+lis[j])
        
        return max(lis)


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
