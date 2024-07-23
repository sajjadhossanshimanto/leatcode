#%%
from typing import List
from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for ln in range(1, len(nums)):
            ans.extend(combinations(nums, r=ln))

        ans.append(nums)
        return ans

# %%
Solution().subsets([1, 2, 3])
# %%
