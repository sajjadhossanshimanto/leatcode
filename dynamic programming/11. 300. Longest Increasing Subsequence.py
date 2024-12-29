# https://leetcode.com/problems/longest-increasing-subsequence/

#%%
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for i in nums:
            while stack and i <= stack[-1]:
                stack.pop()
            stack.append(i)
        return len(stack)

# %%
s = Solution()
s.lengthOfLIS(
    [7,7,7,7,7,7,7]
)
# %%
# ans: 4
s.lengthOfLIS(
    [0,1,0,3,2,3]
)
# %%
