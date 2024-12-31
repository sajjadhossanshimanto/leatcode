# https://leetcode.com/problems/coin-change-ii/description/

#%%
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # path counting proablem
        # but only unique path
        coins.sort()
        cache = {}
        def dfs(money_left, start=0) -> List[List[int]]:# number of ways
            # if money_left in cache: return cache[money_left]
            if start>=len(coins): return []

            paths=[]
            for pos in range(start, len(coins)):
                i = coins[pos]
                if money_left-i==0:
                    paths.append([i])
                elif money_left-i<0:
                    continue
                else:
                    for path in dfs(money_left-i, pos):
                        path.append(i)
                        paths.append(path)

            # cache[money_left] = paths
            return paths
        
        
        return len(dfs(amount))

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
