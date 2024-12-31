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
# ans: 5
# out: 9 as it contain replacement
s.change(
    amount = 10, coins = [5, 2, 1]
)
# %%
s.change(
    amount = 3, coins = [2]
)
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
