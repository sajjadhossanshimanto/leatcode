'''
https://leetcode.com/problems/combination-sum/description/
- one item can be used multiple time
'''
#%%
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        def backtrack(start: int, pre_sum: int, path: list) -> list[int, list]:
            if start>=len(candidates): return
            if pre_sum>=target: return

            for pos in range(start, len(candidates)):
                total = pre_sum + candidates[pos]
                path.append(candidates[pos])
                if total<target:
                    backtrack(pos, total, path)
                elif total==target:
                    res.append(path[:])
                path.pop()

        backtrack(0, 0, [])
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
