#%%
from typing import List
from itertools import combinations



inf = float('inf')
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # def comb()
        n=len(s)
        low = num# TODO: str inf. can be set to `num` if it is guranged k would be at least 1

        for i in combinations(num, r=len(num)-k):
            low = min("".join(i), low)
        
        return low

s = Solution()
# %%
s.removeKdigits('1432219', k=3)
# %%
s.removeKdigits("10200", k=1)
# %%
s.removeKdigits("10", 2)
# %%
