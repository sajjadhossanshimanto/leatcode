#%%
from typing import List
from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums = tuple(nums)
        ans = {tuple()}
        for ln in range(1, len(nums)):
            ans.update(combinations(nums, r=ln))

        ans.add(nums)
        return ans

# %%
Solution().subsets([1, 2, 3])
# %%
Solution().subsets([1, 2, 2])
# %%
Solution().subsets([0])
# %%
