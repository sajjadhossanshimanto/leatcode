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
# [ [1,1,6], [1,2,5], [1,7], [2,6] ]
s.combinationSum(candidates = [10,1,2,7,6,1,5], target = 8)
# %%
# [ [1,2,2], [5] ]
s.combinationSum(candidates = [2,5,2,1,2], target = 5)
#%%