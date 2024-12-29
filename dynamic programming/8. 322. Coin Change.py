# https://leetcode.com/problems/coin-change/description/

#%%
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        count = 0
        for i in range(len(coins)-1, -1, -1):
            if amount<coins[i]: continue
            c, amount=divmod(amount, coins[i])
            count+=c
        
        return count if amount==0 else -1

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

#%%
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        count = 0
        for i in range(len(coins)-1, -1, -1):
            if amount<coins[i]: continue
            c, amount=divmod(amount, coins[i])
            count+=c
        
        return count if amount==0 else -1

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
