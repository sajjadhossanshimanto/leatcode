# https://leetcode.com/problems/maximum-product-subarray/description/

#%%
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        suffix = 1
        prefix = 1
        max_ = max(nums)
        n = len(nums)
        for i in range(n):
            if suffix==0: suffix = 1
            if prefix==0: prefix = 1

            prefix *= nums[i]
            suffix *= nums[n-i-1]

            max_ = max(prefix, suffix, max_)

        return  max_
# %%
s = Solution()
s.maxProduct(
    [2,3,-2,4]
)
# %%
s.maxProduct(
    [-2,0,-1]
)
# %%
