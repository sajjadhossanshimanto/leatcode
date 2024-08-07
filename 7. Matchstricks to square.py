'''
https://leetcode.com/problems/matchsticks-to-square/
'''
#%%
from typing import List
from itertools import combinations


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks)<4: return False

        side, remin = divmod(sum(matchsticks), 4)# O(n)
        if remin: return False

        matchsticks.sort()# O(n)
        # error: we can't bend any stick
        if matchsticks[-1]>side: return False

        sides = [side]*4
        while matchsticks:
            stick = matchsticks.pop()
            if stick==side: sides.pop()
            else:
                # error: there are stick left but no place
                if not sides: return False
                
                # find a proper pos to place stick
                pos = len(sides) - 1
                while pos>=0:
                    if sides[pos] > stick:
                        break
                    pos -=1
                else:
                    # error: no place found to place
                    return False
                
                sides[pos] -= stick
                if sides[pos]==0: sides.pop(pos)
        
        return True

s = Solution()
# %%
# ans = 1
s.makesquare([1,1,2,2,2])
# %%
# ans = 0
s.makesquare([3,3,3,3,4])
# %%
