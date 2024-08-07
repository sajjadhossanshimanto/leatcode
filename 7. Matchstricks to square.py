'''
https://leetcode.com/problems/matchsticks-to-square/
'''
#%%
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks)<4: return False

        target, remin = divmod(sum(matchsticks), 4)# O(n)
        if remin: return False

        matchsticks.sort()# O(n)
        # error: we can't bend any stick
        if matchsticks[-1]>target: return False

        res = [0]
        visit = [0]*len(matchsticks)
        def backtrack(start: int, pre_sum: int) -> list[int, list]:
            if start>=len(matchsticks): return # base case: end of tree

            for pos in range(start, len(matchsticks)):
                i = matchsticks[pos]
                if visit[pos]: continue

                total = pre_sum + i
                visit[pos] = 1
                if total<target:
                    preserve = backtrack(pos+1, total)
                elif total>target:
                    preserve = False
                elif total==target:
                    # TODO: ensure donot remove from visit
                    res[0] += 1
                    preserve = True
                
                if preserve:
                    if pre_sum!=0:# preserve root
                        return True
                else:
                    visit[pos] = 0

        backtrack(0, 0)

        return res[0]==4

s = Solution()
# %%
# ans = 1
s.makesquare([1,1,2,2,2])
# %%
# ans = 0
s.makesquare([3,3,3,3,4])
# %% wa176
# ans = 1
# out = 0
s.makesquare([5,5,5,5,4,4,4,4,3,3,3,3])
# distribution should be -> 5+4+3 on each side
# but mine substrack all larges 
# %%
