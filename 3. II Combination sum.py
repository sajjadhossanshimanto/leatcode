#%%
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = set()
        def backtrack(start: int, pre_sum: int, path: list) -> list[int, list]:
            if start>=len(candidates): return
            if pre_sum>=target: return

            for pos in range(start+1, len(candidates)):
                total = pre_sum + candidates[pos]
                path.append(candidates[pos])
                if total<target:
                    backtrack(pos, total, path)
                elif total==target:
                    res.add(tuple(path))
                path.pop()

        backtrack(-1, 0, [])
        return res

s = Solution()
# %%
# [ [1,1,6], [1,2,5], [1,7], [2,6] ]
s.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8)
# %%
# [ [1,2,2], [5] ]
s.combinationSum2(candidates = [2,5,2,1,2], target = 5)
#%%