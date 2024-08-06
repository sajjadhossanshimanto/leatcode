'''
https://leetcode.com/problems/combination-sum-ii/description/
- can't use samne item twice
- res should not contain dublicate as
- input may contain dulicate
'''
#%%
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        def backtrack(start: int, pre_sum: int, path: list) -> list[int, list]:
            if start>=len(candidates): return
            if pre_sum>=target: return

            for pos in range(start, len(candidates)):
                i = candidates[pos]
                if i>start and i == candidates[pos-1]: continue

                total = pre_sum + i
                path.append(i)
                if total<target:
                    backtrack(pos+1, total, path)
                elif total==target:
                    res.append(tuple(path))
                path.pop()

        backtrack(0, 0, [])
        return res

s = Solution()
# %%
# [ [1,1,6], [1,2,5], [1,7], [2,6] ]
s.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8)
# %%
# [ [1,2,2], [5] ]
s.combinationSum2(candidates = [2,5,2,1,2], target = 5)
#%% TL172
s.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 30)
# %%
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(target, start, comb):
            if target < 0:
                return
            if target == 0:
                res.append(comb)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                dfs(target-candidates[i], i+1, comb+[candidates[i]])

        dfs(target, 0, [])
        return res
# %%
