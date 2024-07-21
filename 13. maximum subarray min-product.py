#%%
from typing import List


inf = float('inf')
class Solution:
    def maxSumMinProduct(self, num: List[int]) -> int:
        total = 0
        minmum = inf
        for i in num:
            total+=i
            minmum = min(minmum, i)
        
        # mul & mod
        ans = 0
        mod = 10e9+7# TODO: why +7
        for _ in range(minmum):
            ans+=total
            if ans>mod:
                ans-=mod

s = Solution()
# %%
