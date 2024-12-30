# https://leetcode.com/problems/unique-paths/description/

#%%
from functools import lru_cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache(None)
        def dfs(x, y):
            if x==m-1 and y==n-1:
                return 1

            if x>=m or y>=n: return 0

            return dfs(x+1, y) + dfs(x, y+1)

        return dfs(0, 0)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        
        # loop will iterate through doted lines
        # 1111
        # 1---
        # 1---
        for i in range(1, m):# note: zero is skipped
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        # The bottom-right corner contains the result
        return dp[m - 1][n - 1]

s = Solution()
# %%
s.uniquePaths(m = 3, n = 7)
# %%
s.uniquePaths(3, 2)
# %% tl
s.uniquePaths(23, 12)

# %%
