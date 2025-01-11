# https://leetcode.com/problems/binary-search/

#%%
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (r+l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

s = Solution()
# %%
# 4
s.search(nums = [-1,0,3,5,9,12], target = 9)
# %%
# -1
s.search(nums = [-1,0,3,5,9,12], target = 2)
# %%
s.search([5], )