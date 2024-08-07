'''
https://leetcode.com/problems/matchsticks-to-square/
'''
#%%
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        if n<4: return False

        target, remin = divmod(sum(matchsticks), 4)# O(n)
        if remin: return False

        # matchsticks.sort()# O(nlogn)
        # error: we can't bend any stick
        if max(matchsticks)>target: return False

        visit = [0]*n
        def backtrack(i, k, pre_sum):
            if k==0:
                return True
            if pre_sum==target:
                # start checking from zero 
                return backtrack(0, k-1, 0)

            # starting from i
            for i in range(i, n):
                if visit[i] or matchsticks[i] + pre_sum > target: continue

                visit[i] = 1
                if backtrack(i+1, k, pre_sum + matchsticks[i]):
                    return True
                visit[i] = 0
            
            return False

        return backtrack(0, 4, 0)

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
