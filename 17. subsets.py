#%%
from typing import List
from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for ln in range(1, len(nums)):
            for i in range(0, len(nums)-ln+1):
                ans.append(nums[i:i+ln])
                # print([i, i+ln])
        ans.append(nums)
        return ans

# %%
Solution().subsets([1, 2, 3])
# %%