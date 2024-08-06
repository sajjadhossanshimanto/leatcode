#%%
from typing import List
from itertools import combinations


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        filter(lambda x:x>target, candidates)

        res = []
        for i in range(1, len(candidates)):
            res.extend(
                filter(
                    lambda x:sum(x)==target,# TODO generate sum on the go
                    combinations(candidates, r=i)
                )
            )

        return res

s = Solution()
# %%
# Output: [[2,2,3], [7]]
s.combinationSum([2, 3, 6, 7], 7)
# %%
# Output: [[2,2,2,2],[2,3,3],[3,5]]
s.combinationSum([2, 3, 5], 8)
# %%
# []
s.combinationSum([2], 1)
# %%
