'''
https://leetcode.com/problems/baseball-game/description/
'''
#%%
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for i in operations:
            if i=="C":
                scores.pop()
            elif i=="D":
                scores.append(scores[-1]*2)
            elif i=="+":
                scores.append(scores[-1] + scores[-2])
            else:
                scores.append(int(i))
        
        return sum(scores)


s = Solution()
#%%
# ans = 30
s.calPoints(operations=["5", "2", "C", "D", "+"])
# %%
# ans = 27
s.calPoints(["5","-2","4","C","D","9","+","+"])
# %%
# 0
s.calPoints(["1","C"])
# %%
