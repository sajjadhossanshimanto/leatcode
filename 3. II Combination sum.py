#%%
from typing import List
from itertools import combinations_with_replacement


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        filter(lambda x:x>target, candidates)

        res = []
        for i in range(1, len(candidates)):
            res.extend(
                filter(
                    lambda x:sum(x)==target,# TODO generate sum on the go
                    combinations_with_replacement(candidates, r=i)
                )
            )

        return res

s = Solution()
# %%
s.combinationSum([2, 3, 6, 7], 7)
# %%
s.combinationSum([10, 1, 2, 7, 6, 1, 5], 8)
# %%
