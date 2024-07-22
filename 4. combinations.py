#%%
from typing import List
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1, n+1), r=k))

s = Solution()
# %%
s.combinationSum(4, 2)
# %%
