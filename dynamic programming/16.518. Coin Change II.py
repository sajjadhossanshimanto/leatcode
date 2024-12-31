# https://leetcode.com/problems/coin-change-ii/description/

#%%
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # path counting proablem
        # but only unique path
        unique_paths = set()
        cache = {}
        def dfs(money_left, path=[]) -> int:# number of ways
            # if money_left in cache: return cache[money_left]
            if money_left==0:
                unique_paths.add(tuple(sorted(path)))
                return 1
            if money_left<0: 
                return 0

            count = 0
            for i in coins:
                # print(i, end=" ")
                path.append(i)
                count+=dfs(money_left-i, path)
                path.pop()
            
            # cache[money_left] = count
            return count
        
        
        return len(unique_paths)

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
