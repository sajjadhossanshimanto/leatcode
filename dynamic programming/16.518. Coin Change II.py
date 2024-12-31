# https://leetcode.com/problems/coin-change-ii/description/

#%%
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # path counting proablem
        # but only unique path
        
        def dfs(money_left) -> int:# number of ways
            if money_left==0: 
                # print(" end point hit")
                return 1
            if money_left<0: 
                return 0

            count = 0
            for i in coins:
                # print(i, end=" ")
                count+=dfs(money_left-i)
            return count
        
        return dfs(amount)

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
