'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
#%%
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        ans = 0
        for i in prices:
            profit = 0
            while stack and stack[-1][0] <= i :
                prev = stack.pop()
                profit = (i - prev[0]) + prev[1]
            ans = max(ans, profit)
            stack.append((i, profit))
        
        return ans

s = Solution()
# %%
# 5 ==> 1 -> 6
s.maxProfit([7,1,5,3,6,4])
# %%
# 0
s.maxProfit([7,6,4,3,1])
# %%
