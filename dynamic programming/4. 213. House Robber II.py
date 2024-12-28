# https://leetcode.com/problems/house-robber-ii/description/

#%%
from typing import List
from functools import lru_cache
from itertools import islice


def print_return(func):
    def deco(*args, **kwargs):
        r = func(*args, **kwargs)
        print(f"return -> {r} for args: {args}, kwargs: {kwargs}")
        return r
    return deco

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]

        @lru_cache
        # @print_return
        def rob(start, end=len(nums)):
            if end-start<=2: return max(nums[start:end])

            return max(
                nums[start] + rob(start+2, end),
                rob(start+1, end)
            )
        
        return max(rob(0, len(nums)-1), rob(1, len(nums)))


#%%
s = Solution()
s.rob(
    [6,3,10,8,2,10,3,5,10,5,3]
#    [0,1,2,3,4,5,6,7,8,9,10]
)
# %%
# wa -> ans: 4 out: 3
s.rob(
    [1,2,3,1]
)
# %%
