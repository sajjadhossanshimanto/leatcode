'''
https://leetcode.com/problems/combinations/description/
'''
#%%
from typing import List
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1, n+1), r=k))

s = Solution()
# %%
# [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
s.combine(4, 2)
# %%
s.combine(1, 1)
# %%
