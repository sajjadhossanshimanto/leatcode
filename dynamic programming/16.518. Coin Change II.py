# https://leetcode.com/problems/coin-change-ii/description/

#%%
from typing import List
from functools import lru_cache


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        @lru_cache(None)
        def dfs(money_left):
            if money_left==0: return 1

            count = 0
            for i in coins:
                if i>money_left: break

                count+=dfs(money_left-i)
            
            return count

        return dfs(amount)

s = Solution()
# %%
# ans: 5
# out: 9 as it contain replacement
s.change(
    amount = 5, coins = [5, 2, 1]
)
# %%
s.change(
    amount = 3, coins = [2]
)

#%%
## solution by neetcode
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(i, money_left):
            if (i, money_left) in cache: return cache[(i, money_left)]

            if money_left==0: return 1
            if money_left<0: return 0

            if i==len(coins): return 0

            cache[(i, money_left)] = dfs(i, a+coins[i]) + dfs(i+1, a)

s = Solution()

# %%
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Dynamic Programming approach
        # dp[i] represents the number of ways to make up the amount `i`
        dp = [0] * (amount + 1)
        dp[0] = 1  # There is one way to make amount 0, which is using no coins

        # Iterate over each coin
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
                # print(f"coin={coin}, i={i}", dp)

        return dp[amount]

s = Solution()
s.change(
    amount = 5, coins = [2, 1, 5]
)
# %%
