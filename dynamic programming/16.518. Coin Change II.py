# https://leetcode.com/problems/coin-change-ii/description/

#%%
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # path counting proablem
        # but only unique path
        
        # coins.sort()
        cache = {}
        def dfs(money_left, start=0) -> int:# number of ways
            # if money_left in cache: return cache[money_left]
            if start>=len(coins): return 0

            counter = 0
            for pos in range(start, len(coins)):
                i = coins[pos]
                if money_left-i==0:
                    counter += 1
                elif money_left-i<0:
                    continue
                else:
                    counter+=dfs(money_left-i, pos)

            # cache[money_left] = paths
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
