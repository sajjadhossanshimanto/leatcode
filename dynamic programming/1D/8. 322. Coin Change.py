# https://leetcode.com/problems/coin-change/description/

#%%
from typing import List
from functools import lru_cache


inf = float("inf")
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dfs(money):
            if money==0: return 0
            
            count = inf
            for i in coins:
                if money>=i:
                    count = min(dfs(money-i)+1, count)
            
            return count
        
        result = dfs(amount)
        return result if result != inf else -1

# %%
s= Solution()
s.coinChange(
    coins = [1,2,5], amount = 11
)
# %%
s.coinChange(
    coins = [2], amount = 3
)
# %%
s.coinChange(
    coins = [1], amount = 0
)
# %% wa -> 408 may devide given ammount better than 419
s.coinChange(
    [186,419,83,408],
    6249
)
# %%
