# https://leetcode.com/problems/partition-equal-subset-sum/

#%%
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        half = sum(nums)/2
        sub_set = set([0])
        for i in nums:
            for j in list(sub_set): # RuntimeError: Set changed size during iteration
                sub_set.add(i+j)
                if i+j==half: return True
        return False

# %%
s = Solution()
s.canPartition(
    [1,2,3,5]
)
# %%
