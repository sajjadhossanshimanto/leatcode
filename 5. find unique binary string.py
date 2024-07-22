#%%
from typing import List
from itertools import combinations


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        nums = set(nums)
        for i in range(int("1"+"0"*n, base=2)):
            b = format(i, "b")
            b = "0"*(n-len(b)) + b
            if b not in nums:
                return b

s = Solution()
# %%
s.findDifferentBinaryString(["00", "01"])
# %%
