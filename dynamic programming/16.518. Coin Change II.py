# https://leetcode.com/problems/coin-change-ii/description/

#%%
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # path counting proablem
        # but only unique path
        if amount==0: return 1
        
        cache = {}
        # dfs number of inputs represents --> dimention
        # 2 inputs means 2d
        # every dfs with caching can be represented as dynamic programming
        def dfs(money_left, start=0) -> int:# number of ways
            if (money_left, start) in cache: return cache[(money_left, start)]
        
            if start>=len(coins) or money_left<0: return 0
            if money_left==0: return 1

            counter = 0
            for pos in range(start, len(coins)):
                i = coins[pos]
                counter+=dfs(money_left-i, pos)

            cache[(money_left, start)] = counter
            return counter


        return (dfs(amount))

s = Solution()
# %%
# ans: 5
# out: 9 as it contain replacement
s.change(
    amount = 5, coins = [1, 2,5]
)
# %%
s.change(
    amount = 3, coins = [2]
)
# %%
