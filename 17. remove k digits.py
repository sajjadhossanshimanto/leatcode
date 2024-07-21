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
s='1432219'
l = combinations(s, r=7)
list(l)
# %%
"12">"90"
# %%
def combinations(l, r):
    l = list(l)
    # TODO: how this function is desiged
    index = 
    for removal in range(len(r), 0, -1):
        for i in range(0, len(l)-r):
            print(index+str(i))

combinations([1, 2, 3, 4, 5], 3)
# %%
