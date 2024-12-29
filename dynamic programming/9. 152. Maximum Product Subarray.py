# https://leetcode.com/problems/maximum-product-subarray/description/

#%%
from itertools import combinations
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_mul = 0
        for i in range(1, len(nums)):
            for j in combinations(nums, i):
                mul = 1
                for k in j: mul*=k
                if mul>max_mul: max_mul = mul
        
        return max_mul

# %%
# ans: 6
s = Solution()
s.maxProduct(
    [2,3,-2,4]
)
# %%
